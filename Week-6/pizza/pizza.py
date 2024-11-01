import csv,os,sys
from tabulate import tabulate
def main():
    file=sys.argv
    chart=check_file(file)
    chart_making(chart)

def check_file(file):
    try:
        if len(file) > 2:
            sys.exit("Too many command-line arguments")
        if ".csv" in file[1] and os.path.exists(file[1]):
            return file [1]
        elif ".csv" in file[1] and (os.path.exists(file[1]) == False):
            sys.exit("File do not exist")
        else:
            sys.exit("Not a csv file")
    except IndexError:
        sys.exit("Too few command-line arguments")

def chart_making(chart):
        with open(chart) as chart:
            reader=csv.reader(chart)
            headers = next(reader)
            print(tabulate(reader,headers,tablefmt="grid"))

main()