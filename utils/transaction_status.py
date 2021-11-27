from enum import Enum


class TransactionStatus(Enum):
    INCOMPLETE = 1
    COMMITTED = 2
    ABORTED = 3
