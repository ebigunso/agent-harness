import pytest
from src.ids import parse_id


def test_numeric_ok():
    assert parse_id(" 123 ") == "123"


def test_alpha_rejected():
    with pytest.raises(ValueError):
        parse_id("abc")
