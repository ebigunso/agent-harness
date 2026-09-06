import re

_ID_RE = re.compile(r"^[0-9]+$")


def parse_id(raw: str) -> str:
    """Validate and normalize a record id. Returns the canonical id string."""
    raw = raw.strip()
    if not _ID_RE.match(raw):
        raise ValueError(f"invalid id: {raw!r}")
    return raw
