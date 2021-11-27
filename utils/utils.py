from typing import List, Tuple

from data.data import Data
from operations.operations import Operation, WriteOperation, ReadOperation
from transaction.transaction import Transaction


def create_transactions(operations: List[Operation]) -> List[Transaction]:
    result: List[Transaction] = []
    transactions = dict()
    for operation in operations:
        if operation.transaction not in transactions.keys():
            transactions[operation.transaction] = [operation]
        else:
            transactions[operation.transaction].extend([operation])

    for transaction in transactions.keys():
        result.append(Transaction(transaction_id=transaction, operations=transactions[transaction]))

    return result


def create_dummy_schedule() -> Tuple[List[Data], List[Operation]]:
    data_a = Data(data_name="A", data_value=1)
    data_b = Data(data_name="B", data_value=2)
    data_c = Data(data_name="C", data_value=3)

    op_1 = WriteOperation(transaction=1, target_data=data_a, new_value=5)
    op_2 = ReadOperation(transaction=2, target_data=data_b)
    op_3 = WriteOperation(transaction=1, target_data=data_c, new_value=2)
    op_4 = WriteOperation(transaction=3, target_data=data_c, new_value=765)
    op_5 = ReadOperation(transaction=2, target_data=data_b)

    data = [data_a, data_b, data_c]
    ops = [op_1, op_2, op_3, op_4, op_5]
    return data, ops
