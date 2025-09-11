from twttr import shorten

def test_uppers():
    assert shorten("AEIOU") == ""
    assert shorten("are YOU there") == "r Y thr"

def test_lowers():
    assert shorten("aeiou") == ""

def test_numbers():
    assert shorten("12345") == "12345"

def test_puncs():
    assert shorten("...") == "..."
