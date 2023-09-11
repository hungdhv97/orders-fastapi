from enum import Enum


class BillStatusEnum(str, Enum):
    UNPAID = 'unpaid'
    PAID = 'paid'
