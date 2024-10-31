import sys
import os


def main():
    file = sys.argv
    check_file(file)
    file = file[1]
    print(read_lines(file))


def check_file(file):
    try:
        if len(file) > 2:
            sys.exit("Too many command-line arguments")
        if ".py" in file[1] and os.path.exists(file[1]):
            pass
        elif ".py" in file[1] and (os.path.exists(file[1]) == False):
            sys.exit("File do not exist")
        else:
            sys.exit("Not a python file")
    except IndexError:
        sys.exit("Too few command-line arguments")


def read_lines(file):
    qnt_linhas = 0
    with open(file) as file:
        for row in file:
            if row.lstrip().startswith("#"):
                continue
            if row.strip() == "":
                continue
            else:
                qnt_linhas += 1
    return qnt_linhas


main()
