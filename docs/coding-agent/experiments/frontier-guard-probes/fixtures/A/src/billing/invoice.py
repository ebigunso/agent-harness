from dataclasses import dataclass
from src.core.money import Money


@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    currency: str  # ISO 4217, e.g. "USD"
    total: Money
