import csv
import io
from src.reports.summary import build_summary


def export_csv(invoices) -> str:
    s = build_summary(invoices)
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(list(s.keys()))
    w.writerow(list(s.values()))
    return buf.getvalue()
