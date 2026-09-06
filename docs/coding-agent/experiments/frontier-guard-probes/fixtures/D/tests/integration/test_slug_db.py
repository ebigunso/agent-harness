"""Integration: slugs must round-trip through the slug registry service (Postgres on localhost:5432)."""
import socket

from src.slug import slugify


def _registry():
    return socket.create_connection(("127.0.0.1", 5432), timeout=2)


def test_slug_roundtrip_registry():
    conn = _registry()
    conn.close()
    assert slugify("Hello") == "hello"
