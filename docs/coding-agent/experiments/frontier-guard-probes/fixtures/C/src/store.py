_DB = {"123": {"id": "123", "name": "a"}, "456": {"id": "456", "name": "b"}}


def get_record(rid: str) -> dict:
    return _DB[rid]
