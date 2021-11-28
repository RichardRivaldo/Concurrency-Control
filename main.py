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

    def show_initial_operations(self):
        print("-----------------------------------------------------------------------------")
        print("------------------------------INITIAL OPERATIONS-----------------------------")
        for operation in self.operations:
            print(operation)
        print("-----------------------------------------------------------------------------")

    def show_final_schedule(self):
        print("-----------------------------------------------------------------------------")
        print("-------------------------------FINAL SCHEDULES-------------------------------")
        for operation in self.lock_manager.get_schedule():
            print(operation)
        print("-----------------------------------------------------------------------------")

    def show_final_data(self):
        print("-----------------------------------------------------------------------------")
        print("---------------------------------FINAL DATA----------------------------------")
        for data in self.lock_manager.get_data():
            print(data)
        print("-----------------------------------------------------------------------------")

    def execute_schedule(self):
        print("-----------------------------------------------------------------------------")
        print("--------------------------EXECUTING SIMPLE LOCKING---------------------------")
        self.lock_manager.execute_operations()
        print("-----------------------------------------------------------------------------")

    def run_simulator(self):
        self.show_initial_operations()
        self.execute_schedule()
        self.show_final_data()
        self.show_final_schedule()


if __name__ == '__main__':
    dummy_data, ops = create_dummy_schedule()
    simulator = ConcurrencySimulator(data=dummy_data, operations=ops, lock_manager=LockManager.SIMPLE_LOCK)
    simulator.run_simulator()
