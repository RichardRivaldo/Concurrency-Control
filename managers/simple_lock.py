# Simple Locking - Exclusive Locks Only
# Rigorous Two-Phase Locking -> release locks only when aborting or committing the transaction
from typing import List, Dict

from data.data import Data
from operations.operations import Operation
from transaction.transaction import Transaction
from utils.lock_mode import LockMode
from utils.utils import create_transactions


class SimpleLockManager:
    def __init__(self, data: List[Data], operations: List[Operation]) -> None:
        self.data: List[Data] = data
        self.operations: List[Operation] = operations
        self.transactions: List[Transaction] = create_transactions(self.operations)

        self.locks: Dict[str, int] = dict()
        self.schedule: List[Operation] = []

    def is_locked(self, requested_data: str, requesting_transaction: int):
        if requested_data in self.locks.keys():

            locking_transaction = self.locks[requested_data]
            # Locked by another transaction
            if locking_transaction != requesting_transaction:
                return True
        # Locked by the requesting transaction or unlocked
        return False

    def grant_lock(self, requested_data: Data, requesting_transaction: int):
        if not self.is_locked(requested_data=requested_data.data_name, requesting_transaction=requesting_transaction):
            # Lock the data to be EXCLUSIVE
            requested_data.set_lock_mode(LockMode.EXCLUSIVE)
            # Update the lock list with the entry
            self.locks[requested_data.data_name] = requesting_transaction
            print(f"Successfully granting lock for data {requested_data.data_name} to T{requested_data}!")
        else:
            print("The data is currently being locked by other transaction!")

    def revoke_lock(self, target_data: Data):
        data_name = target_data.data_name
        self.locks.pop(data_name)
        print(f"Successfully revoked the lock on data {data_name}")

    def create_schedule(self):
        pass
