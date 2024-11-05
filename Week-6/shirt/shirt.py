import os, sys
from PIL import Image, ImageOps


def main():
    file = sys.argv
    check_input(file)
    check_file(file)
    put_shirt()



def check_input(file):
    if len(file) < 3:
        sys.exit("Too few command-line arguments")
    elif len(file) > 3:
        sys.exit("Too many command-line arguments")
    else:
        pass


def check_file(file):
    try:
        script, before, after = sys.argv
        before_name, before_type = before.split(".")
        after_name, after_type = after.split(".")
        types = ["jpg", "jpeg", "png"]
        if before_type in types and after_type in types and after_type == before_type:
            pass
        elif before_type in types and after_type in types and after_type != before_type:
            sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")
    except (IndexError, ValueError):
        sys.exit("Too few command-line arguments")


def put_shirt():
    try:
        script, before, after = sys.argv
        before = Image.open(before)
        after = before.copy()
        shirt = Image.open("shirt.png")
        size = shirt.size
        after = ImageOps.fit(after, size = size)
        after.paste(shirt, shirt)
        after.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
