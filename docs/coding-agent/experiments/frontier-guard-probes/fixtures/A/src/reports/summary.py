from typing import Iterable
from src.billing.invoice import Invoice
from src.core.money import Money


def build_summary(invoices: Iterable[Invoice]) -> dict:
    """Summary consumed by the CSV exporter in src/reports/export.py."""
    total = Money.zero()
    count = 0
    for inv in invoices:
        total = total + inv.total
        count += 1
    return {"count": count, "total": str(total.amount)}
