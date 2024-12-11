from numb3rs import validate


def main():
    test_numb3rs()

def test_numb3rs():
    assert validate("edson") == False
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("5555") == False
    assert validate(",,,,") == False
    assert validate("1.2.3.1000") == False
    assert validate("75.333.45.22") == False



if __name__ == "__main__":
    main()