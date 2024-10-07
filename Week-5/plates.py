def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if (
        starts_with_two_letters(s)
        and max_6_characters(s)
        and numbers_at_end(s)
        and last_check(s)
    ):
        return True
    else:
        return False


def starts_with_two_letters(text):
    return text[0:2].isalpha()


def max_6_characters(text):
    return 2 <= len(text) <= 6


def numbers_at_end(text):
    return (text[-2:].isnumeric() or text[-2:].isalpha()) and (
        True if text.find("0") == -1 else text[text.find("0") - 1].isalpha() == False
    )


def last_check(text):
    return (
        text.strip() == text
        and (text.find(",") == -1 and text.find("'") == -1)
        and text.find(".") == -1
    )

if __name__ == "__main__":
    main()
