from seasons import convert_to_minutes

def main():
    test_seasons()

def test_seasons():
    assert convert_to_minutes("1999-01-01") == 13760640
    assert convert_to_minutes("2024-03-01") == 525600
    assert convert_to_minutes("2023-03-01") == 1052640
    assert convert_to_minutes("2000-08-18") == 12903840


if __name__ == '__main__':
    main()
