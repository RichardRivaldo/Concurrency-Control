# Transaction implementation

from dataclasses import dataclass
from typing import List

from operations.operations import Operation


@dataclass
class Transaction:
    transaction: int
    operations: List[Operation]
    current_operation: int

    def increment_operation_idx(self):
        self.current_operation += 1

    def execute_read(self):
        self.operations[0].execute_read()
        self.increment_operation_idx()

    def execute_write(self):
        self.operations[0].execute_write()
        self.increment_operation_idx()

    def execute_commit(self):
        self.log("The transaction commited successfully!")
        self.increment_operation_idx()

    def execute_abort(self):
        self.log("The transaction is aborted!")
        self.current_operation = 0
