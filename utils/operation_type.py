from enum import Enum


class OperationType(Enum):
    READ = "READ"
    WRITE = "WRITE"
    COMMIT = "COMMIT"
    ABORT = "ABORT"
