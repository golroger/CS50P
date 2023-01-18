from fuel import   gauge
from fuel import convert

import pytest as pt

def main() :
    test_gauge()
    test_convert()
# First function to test gauge funtion in fuel.py with three diffrent possibles values
def test_gauge() :
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
    assert gauge(99) == "F"

def test_convert() :
    assert convert("1/4") == 25
    with pt.raises(ZeroDivisionError) :
        convert("1/0")
    with pt.raises(ValueError) :
        convert("ddd/dee")


if __name__ == "__main__" :
    main()