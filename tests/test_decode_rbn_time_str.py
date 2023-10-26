from datetime import datetime, UTC
from rbnread.rbn_decoder import _decode_rbn_time_str


def test_decode_rbn_time_str():
    # test happy cases
    result = _decode_rbn_time_str("0945Z")
    assert result.minute == 45
    assert result.hour == 9
    assert result.tzinfo == UTC
    result = _decode_rbn_time_str("2359Z")
    assert result.minute == 59
    assert result.hour == 23


def test_decode_rbn_time_str_errors():
    """Run through all the error paths"""
    # empty string
    result = _decode_rbn_time_str("")
    assert result is None
    # long string
    result = _decode_rbn_time_str("12345Z")
    assert result is None
    # invalid string (doesn't end in Z)
    result = _decode_rbn_time_str("12345")
    assert result is None
    # invalid string (characters instead of numbers)
    result = _decode_rbn_time_str("a123Z")
    assert result is None
    # invalid hour
    result = _decode_rbn_time_str("2533Z")
    assert result is None
    # invalid minute
    result = _decode_rbn_time_str("1261Z")
    assert result is None
