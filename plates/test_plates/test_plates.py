from plates import is_valid

def main() :
    test_1()
    test_2()
    test_3()
    test_4()

def test_1() :
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("F3.33") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False

def test_2() :
    assert is_valid("AAAAAAA") == False
    assert is_valid("12345") == False

def test_3():
    assert is_valid("AA232D") == False
    assert is_valid("B") == False
    assert is_valid("Bilalda") == False
    assert is_valid("0BI") == False

def test_4() :
    assert is_valid("/.___22") == False



if __name__ == "__main__" :
    main()

