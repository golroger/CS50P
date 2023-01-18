from um import count

def main() :
    test_count()


def test_count():
    assert count("Hello, um, world") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2

def test_firstum() :
    assert count("Um, hey") == 1
    assert count("um") == 1
def test_ends() :
    assert count("chi haja um") == 1
    assert count("yummy") == 0

if __name__ == "__main__" :
    main()