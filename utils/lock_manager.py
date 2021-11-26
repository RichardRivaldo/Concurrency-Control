from enum import Enum

from managers.simple_lock import SimpleLockManager


class LockManager(Enum):
    SIMPLE_LOCK = SimpleLockManager()
