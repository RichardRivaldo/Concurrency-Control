from enum import Enum


class LockMode(Enum):
    UNLOCKED = 0
    SHARED = 1
    EXCLUSIVE = 2
