# Operation implementation

from data.data import Data
from utils.operation_type import OperationType


class Operation:
    def __init__(self, transaction: int, operation_type: OperationType, target_data: Data = None):
        self.transaction: int = transaction
        self.operation_type: OperationType = operation_type
        self.target_data: Data = target_data

    def log(self, message: str):
        print(f"{self} {message}")

    def execute(self):
        pass

    def get_target_data(self):
        return self.target_data

    def get_transaction(self):
        return self.transaction

    def get_operation_type(self):
        return self.operation_type

    def __repr__(self) -> str:
        if self.target_data:
            return f"[T{self.transaction}: {self.operation_type.value} {self.target_data.get_name()}]"
        return f"[T{self.transaction}: {self.operation_type.value}]"


class ReadOperation(Operation):
    def __init__(self, transaction: int, target_data: Data):
        Operation.__init__(self, transaction=transaction, operation_type=OperationType.READ, target_data=target_data)

    def execute(self):
        self.log(f"{self.target_data}")


class WriteOperation(Operation):
    def __init__(self, transaction: int, target_data: Data, new_value: int):
        Operation.__init__(self, transaction=transaction, operation_type=OperationType.WRITE, target_data=target_data)
        self.new_value: int = new_value

    def __repr__(self):
        return f"[T{self.transaction}: {self.operation_type.value} {self.target_data.get_name()} = {self.new_value}]"

    def execute(self):
        self.target_data.set_value(new_value=self.new_value)
        self.log(f"Successfully wrote the value of the data to {self.new_value}!")


class CommitOperation(Operation):
    def __init__(self, transaction: int):
        Operation.__init__(self, transaction=transaction, operation_type=OperationType.COMMIT)

    def execute(self):
        self.log(f"Transaction {self.get_transaction()} committed successfully!")


class AbortOperation(Operation):
    def __init__(self, transaction: int):
        Operation.__init__(self, transaction=transaction, operation_type=OperationType.ABORT)

    def execute(self):
        self.log(f"Transaction {self.get_transaction()} is aborted!")
