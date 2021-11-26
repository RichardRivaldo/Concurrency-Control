# Data implementation
from dataclasses import dataclass

from utils.lock_mode import LockMode


@dataclass
class Data:
    data_name: str
    data_value: int
    lock_mode: LockMode = LockMode.UNLOCKED

    def get_name(self):
        return self.data_name

    def get_value(self):
        return self.data_value

    def get_info(self):
        return self.get_name, self.get_value

    def get_lock_status(self):
        return self.lock_type

    def set_lock_mode(self, lock_mode: LockMode):
        self.lock_type = lock_mode

    def set_value(self, new_value: int):
        self.data_value = new_value
