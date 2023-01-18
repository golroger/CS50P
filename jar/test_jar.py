import pytest
from jar import Jar

def main() :
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init() :
    j =Jar(23)
    assert j.capacity == 23
    with pytest.raises(ValueError) :
        j2 = Jar(0)
        assert j2.capacity

def test_str() :
    jj = Jar(10)
    assert str(jj) == ""
    jj.deposit(3)
    assert str(jj) == "🍪🍪🍪"
    jj.deposit(3)
    assert str(jj) ==  "🍪🍪🍪🍪🍪🍪"

def test_deposit() :
    h =Jar(5)
    h.deposit(2)
    assert h.size == 2
    with pytest.raises(ValueError) :
        h.deposit(4)

def test_withdraw() :
    d=Jar(10)
    d.deposit(7)
    d.withdraw(5)
    assert d.size == 2
    with pytest.raises(ValueError) :
        d.withdraw(3)

if __name__=="__main__" :
    main()