from enum import Enum


class OrderStatus(str, Enum):
    APPROVED    = "Approved"
    IS_SHOPPING = "Is shopping"
    CANCELLED   = "Cancelled"
    ORDERED     = "Ordered"
    DONE        = "Done"
    REFUNDED    = "Refunded"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)