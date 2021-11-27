# Simple Locking - Exclusive Locks Only
from typing import List

from transaction.transaction import Transaction


class SimpleLockManager:
    def __init__(self, transactions: List[Transaction]) -> None:
        self.transactions = transactions
        self.schedule = []
