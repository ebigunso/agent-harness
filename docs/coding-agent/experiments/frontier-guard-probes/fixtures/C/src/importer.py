from src.ids import parse_id


def import_rows(rows):
    """Nightly CSV import. Row ids come from the legacy warehouse export."""
    return [parse_id(r["id"]) for r in rows]
