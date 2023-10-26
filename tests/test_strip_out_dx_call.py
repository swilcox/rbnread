from rbnread.rbn_decoder import _strip_out_dx_call


def test_strip_out_dx_call():
    """test the _strip_out_dx_call method"""
    result = _strip_out_dx_call("AC0C-2-#:")
    assert result == "AC0C"
    result = _strip_out_dx_call("KM4SII-#:")
    assert result == "KM4SII"
