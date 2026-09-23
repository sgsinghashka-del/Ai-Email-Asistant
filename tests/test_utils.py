from src.utils import validate_email


def test_empty_email():
    assert validate_email("") is not None


def test_short_email():
    assert validate_email("Hi") is not None


def test_valid_email():
    assert validate_email("Please confirm our meeting tomorrow.") is None


def test_large_email():
    assert validate_email("x" * 12001) is not None
