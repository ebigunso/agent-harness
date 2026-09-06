from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    """Monetary amount. Used across billing, reports, and the ledger service."""
    amount: Decimal

    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)

    @classmethod
    def zero(cls) -> "Money":
        return cls(Decimal("0"))
