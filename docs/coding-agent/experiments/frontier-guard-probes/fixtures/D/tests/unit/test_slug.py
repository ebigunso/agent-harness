from src.slug import slugify


def test_basic():
    assert slugify("Hello World!") == "hello-world"


def test_collapses_runs():
    assert slugify("a  --  b") == "a-b"
