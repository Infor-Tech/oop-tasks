from enum import Enum

class TransactionStatus(Enum):
    ORDERED = 1
    PROCESSED = 2
    FAILED = 3
    COMPLETED = 4