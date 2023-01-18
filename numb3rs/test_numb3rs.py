from numb3rs import validate

def main() :
    test_ipv4()
    test_ip()
    test_ipv()

def test_ipv4() :
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.1000") == False

def test_ip():
    assert validate("cat") == False
    assert validate("276.0.22.2") == False

def test_ipv() :
    assert validate("123.233.0") == False
    assert validate("75.456.76.65") == False

if __name__ == "__main__" :
    main()