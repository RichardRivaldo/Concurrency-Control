# Operation implementation
from dataclasses import dataclass

from data.data import Data
from utils.operation_type import OperationType


@dataclass
class Operation:
    transaction: int
    operation_type: OperationType
    target_data: Data

    def log(self, message: str):
        print(
            f"[T{self.transaction}: {self.operation_type.value} {self.target_data.get_name()}] {message}"
        )

    def execute_read(self):
        self.log(f"The data has value of {self.target_data.get_value()}.")

    def execute_write(self, new_value: int):
        self.target_data.set_value(new_value=new_value)
        self.log(f"Successfully wrote the data!")
