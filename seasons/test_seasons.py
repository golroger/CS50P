##Golroger
from seasons import is_valid , convert_minutes
import pytest
def main() :
    test_date_invalid()
    test_convert()


def test_date_invalid() :
    assert is_valid("1999-01-01") == [True,"1999","01","01"]
    assert is_valid("1999-13-01") == [False]
    assert is_valid("1999-12-32") == [False]
    assert is_valid("February 6th, 1998") == [False]

def test_convert():
    assert convert_minutes([True,"1999","01","01"]) == "Twelve million, five hundred thirty-five thousand, two hundred minutes"
    assert convert_minutes([True,"1995","01","01"]) == "Fourteen million, six hundred thirty-nine thousand forty minutes"
    with pytest.raises(SystemExit) :
        convert_minutes([False])

if __name__ == "__main__" :
    main()
