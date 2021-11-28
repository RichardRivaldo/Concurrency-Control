# Simple Locking - Exclusive Locks Only
# Rigorous Two-Phase Locking -> release all locks only when aborting or committing the transaction
# Indirectly also Strict Two-Phase Locking -> All locks are EXCLUSIVE
from typing import List, Dict

from data.data import Data
from operations.operations import Operation, AbortOperation
from transaction.transaction import Transaction
from utils.lock_mode import LockMode
from utils.operation_type import OperationType
from utils.utils import create_transactions


class SimpleLockManager:
    def __init__(self, data: List[Data], operations: List[Operation]) -> None:
        self.data: List[Data] = data
        self.operations: List[Operation] = operations
        self.transactions: Dict[int, Transaction] = create_transactions(self.operations)

        self.locks: Dict[str, int] = dict()
        self.schedule: List[Operation] = []

        self.pending: List[Operation] = []
        self.committed: List[int] = []
        self.aborted: List[Transaction] = []

    def get_schedule(self):
        return self.schedule

    def get_data(self):
        return self.data

    def is_locked(self, requested_data: str, requesting_transaction: int):
        if requested_data in self.locks.keys():
            locking_transaction = self.locks[requested_data]
            # Locked by another transaction
            if locking_transaction != requesting_transaction:
                return True
        # Locked by the requesting transaction or unlocked
        return False

    def is_waiting(self, transaction_id: int):
        return any(op for op in self.pending if
                   op.get_transaction() == transaction_id and op.get_operation_type() != OperationType.COMMIT)

    def is_aborted(self, transaction_id: int):
        return transaction_id in self.aborted

    def grant_lock(self, requested_data: Data, requesting_transaction: int):
        data_name = requested_data.data_name
        if not self.is_locked(requested_data=data_name, requesting_transaction=requesting_transaction):
            # Lock the data to be EXCLUSIVE
            requested_data.set_lock_mode(LockMode.EXCLUSIVE)
            # Update the lock list with the entry
            self.locks[requested_data.data_name] = requesting_transaction
            print(f"Successfully granted lock for data {data_name} to T{requesting_transaction}!")
        else:
            print("The data is currently being locked by other transaction!")
            pass

    def revoke_locks(self, target_transaction: int):
        locks_name = []
        for data_name in self.locks.copy().keys():
            holder = self.locks.get(data_name)
            if holder == target_transaction:
                self.locks.pop(data_name)
                locks_name.append(data_name)
        print(f"Successfully revoked all locks ({', '.join(locks_name)}) for transaction {target_transaction}")

    def remove_aborted_ops(self, copy_ops: List[Operation], transaction_id: int):
        for i in range(len(copy_ops)):
            op = copy_ops[i]
            if op.get_transaction() == transaction_id:
                self.operations.pop(i)

    def can_commit(self, transaction_id: int):
        return not any(op for op in self.operations if op.get_transaction() == transaction_id)

    def execute_operations(self):
        while self.operations or self.pending:
            if self.pending:
                head = self.pending[0]
                head_trans_id = head.get_transaction()
                head_target = head.get_target_data()
                op_type = head.get_operation_type()
                if op_type == OperationType.READ or op_type == OperationType.WRITE:
                    if not self.is_locked(requested_data=head.get_target_data().data_name,
                                          requesting_transaction=head_trans_id):
                        print(
                            f"Lock on {head_target.get_name()} is released! Transaction {head_trans_id} will continue!")
                        self.grant_lock(requested_data=head_target,
                                        requesting_transaction=head.get_transaction())
                        head.execute()
                        self.pending.pop(0)
                        self.schedule.append(head)
                        continue
                else:
                    self.pending.pop(0)
                    head.execute()
                    self.revoke_locks(head.get_transaction())
                    self.schedule.append(head)
                    continue
            # Enter this if the pending queue is empty
            operation = self.operations.pop(0)
            transaction_id = operation.get_transaction()
            operation_type = operation.get_operation_type()

            if operation_type == OperationType.COMMIT:
                if self.is_waiting(transaction_id=transaction_id):
                    self.pending.append(operation)
                else:
                    operation.execute()
                    self.revoke_locks(transaction_id)
                    self.committed.append(transaction_id)
                    self.schedule.append(operation)
            else:
                target_data = operation.get_target_data()
                data_name = target_data.data_name if target_data else ""
                if not self.is_locked(requested_data=data_name, requesting_transaction=transaction_id):
                    self.grant_lock(requested_data=target_data, requesting_transaction=transaction_id)
                    operation.execute()
                    self.schedule.append(operation)
                else:
                    transaction = self.transactions.get(transaction_id)
                    ops_count = transaction.get_ops_count()
                    if ops_count <= 1:
                        print(f"Transaction {transaction_id} will wait until lock on {data_name} is released!")
                        self.pending.append(operation)
                    else:
                        abort_operation = AbortOperation(transaction=transaction_id)
                        abort_operation.execute()
                        self.schedule.append(abort_operation)
                        self.remove_aborted_ops(copy_ops=self.operations.copy(), transaction_id=transaction_id)
                        self.revoke_locks(target_transaction=transaction_id)
                        self.operations.extend(transaction.get_operations())
