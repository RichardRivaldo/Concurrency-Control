from typing import List, Tuple, Dict

from data.data import Data
from operations.operations import Operation, WriteOperation, ReadOperation, CommitOperation
from transaction.transaction import Transaction


def create_transactions(operations: List[Operation]) -> Dict[int, Transaction]:
    ops_trans: Dict[int, List[Operation]] = dict()
    transactions: Dict[int, Transaction] = dict()
    for operation in operations:
        transaction_id = operation.get_transaction()
        if transaction_id not in ops_trans.keys():
            ops_trans[transaction_id] = [operation]
        else:
            ops_trans[transaction_id].extend([operation])

    for transaction in ops_trans.keys():
        transactions[transaction] = Transaction(transaction_id=transaction, operations=ops_trans.get(transaction))

    return transactions


def create_dummy_schedule() -> Tuple[List[Data], List[Operation]]:
    data_a = Data(data_name="A", data_value=1)
    data_b = Data(data_name="B", data_value=2)
    data_c = Data(data_name="C", data_value=3)

    # op_0 = ReadOperation(transaction=1, target_data=data_a)
    op_1 = WriteOperation(transaction=3, target_data=data_a, new_value=5)
    op_2 = ReadOperation(transaction=2, target_data=data_c)
    op_3 = WriteOperation(transaction=1, target_data=data_a, new_value=2)
    op_4 = WriteOperation(transaction=3, target_data=data_c, new_value=765)
    op_5 = ReadOperation(transaction=2, target_data=data_a)
    op_6 = CommitOperation(transaction=2)
    op_7 = CommitOperation(transaction=1)
    op_8 = CommitOperation(transaction=3)

    data = [data_a, data_b, data_c]
    ops = [op_1, op_2, op_3, op_4, op_5, op_6, op_7, op_8]
    return data, ops
