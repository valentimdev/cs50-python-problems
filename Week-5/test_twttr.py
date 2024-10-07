from twttr import shorten
def main():
    test_twttr()

def test_twttr():
    assert shorten("edson") == "dsn"
    assert shorten("palavra") == "plvr"
    assert shorten("valentim") == "vlntm"
    assert shorten("5555") == "5555"
    assert shorten(",,,,") == ",,,,"

if __name__ == "__main__":
    main()