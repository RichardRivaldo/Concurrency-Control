# Transaction implementation

from dataclasses import dataclass
from typing import List

from operations.operations import Operation


@dataclass
class Transaction:
    transaction_id: int
    operations: List[Operation]

    def __repr__(self) -> str:
        return f"[T{self.transaction_id}]"

    def log(self, message: str):
        print(f"{self} {message}")

    def get_operations(self):
        return self.operations

    def get_ops_count(self):
        # Total operations - 1, that is Commit Operation
        return len(self.operations) - 1
