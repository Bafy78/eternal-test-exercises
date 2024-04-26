def test_convert_to_integer():
    from number_list import convert_to_integer
    assert convert_to_integer(["a",12.0,13,14.2,"le"]) == [12,13,14]