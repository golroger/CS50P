from twttr import shorten



def test_twttr() :
    assert shorten("Bilal") == "Bll"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS5AAA0") == "CS50"


