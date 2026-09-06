from decimal import Decimal
from src.billing.invoice import Invoice
from src.core.money import Money
from src.reports.summary import build_summary


def _inv(i, cur, amt):
    return Invoice(invoice_id=f"INV-{i}", currency=cur, total=Money(Decimal(amt)))


def test_summary_counts_and_totals():
    s = build_summary([_inv(1, "USD", "10.00"), _inv(2, "USD", "5.50")])
    assert s["count"] == 2
    assert s["total"] == "15.50"
