from data.data import Data
from operations.operations import Operation
from utils.operation_type import OperationType

test = Operation(
    transaction=1,
    operation_type=OperationType.WRITE,
    target_data=Data(data_name="A", data_value=1),
)
test.execute_read()

test2 = Data(data_name="A", data_value=1)
