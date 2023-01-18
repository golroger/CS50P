from plates import is_valid

def main() :
    test_2()

def test_1() :
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_2() :
    assert is_valid("CS50P") == False
    assert is_valid("CSD3") == False

def test_3() :
    assert is_valid("OUTATIME") == False
    assert is_valid("C1234") == False

def test_4() :
    assert is_valid("DK40_30") == False
    assert is_valid("1234567") == False

if __name__ == "__main__" :
    main()