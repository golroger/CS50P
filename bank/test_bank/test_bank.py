from bank import value

def main() :
    test_hello()

def test_hello() :
    assert value("HELLO DAVID") == 0
    assert value("Hello bilal ") == 0

def test_sth() :
    assert value("Hey") == 20
    assert value("haay there what's app ") == 20

def test_nh() :
    assert value("gg") == 100
    assert value("GGG") ==100
    assert value("12341515") ==100


if __name__ == "__main__" :
    main()