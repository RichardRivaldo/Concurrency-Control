# Transaction implementation

from dataclasses import dataclass
from typing import List

from operations.operations import Operation
from utils.transaction_status import TransactionStatus


@dataclass
class Transaction:
    transaction_id: int
    operations: List[Operation]
    current_operation: int = 0
    status: TransactionStatus = TransactionStatus.INCOMPLETE

    def __repr__(self) -> str:
        return f"[T{self.transaction_id}]"

    def log(self, message: str):
        print(f"{self} {message}")

    def set_status(self, new_status: TransactionStatus):
        self.status = new_status

    def increment_operation_idx(self):
        self.current_operation += 1

    def execute(self):
        self.operations[self.current_operation].execute()
        self.increment_operation_idx()

    def execute_abort(self):
        self.current_operation = 0
        self.set_status(TransactionStatus.ABORTED)
        self.log("The transaction committed successfully!")

    def execute_commit(self):
        self.set_status(TransactionStatus.COMMITTED)
        self.log("The transaction is aborted!")
