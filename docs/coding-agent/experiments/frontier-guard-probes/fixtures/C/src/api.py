from src.ids import parse_id
from src.store import get_record


def handle_get(path_param: str) -> dict:
    """GET /records/{id} — public endpoint, see docs/openapi.yaml."""
    rid = parse_id(path_param)
    return get_record(rid)
