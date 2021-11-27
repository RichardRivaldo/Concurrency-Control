from typing import List

from data.data import Data
from managers.simple_lock import SimpleLockManager
from operations.operations import Operation
from utils.lock_manager import LockManager
from utils.utils import create_dummy_schedule


class ConcurrencySimulator:
    def __init__(self, data: List[Data], operations: List[Operation], lock_manager: LockManager):
        self.data = data
        self.operations = operations
        self.lock_manager = self.create_lock_manager(lock_manager)

    def create_lock_manager(self, lock_manager: LockManager):
        if lock_manager == LockManager.SIMPLE_LOCK:
            return SimpleLockManager(data=self.data, operations=self.operations)

    def execute_schedule(self):
        pass


if __name__ == '__main__':
    dummy_data, ops = create_dummy_schedule()
    simulator = ConcurrencySimulator(data=dummy_data, operations=ops, lock_manager=LockManager.SIMPLE_LOCK)
