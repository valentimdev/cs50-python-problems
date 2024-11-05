import csv,os,sys
def main():
    file=sys.argv
    check_file(file)
    file_old=file[1]
    file_new=file[2]
    trade_order(file_old,file_new)
def check_file(file):
    try:
        if len(file) > 3:
            sys.exit("Too many command-line arguments")
        if ".csv" in file[1] and os.path.exists(file[1]):
            pass
        elif ".csv" in file[1] and (os.path.exists(file[1]) == False):
            sys.exit("File do not exist")
        else:
            sys.exit("Not a csv file")
    except IndexError:
        sys.exit("Too few command-line arguments")

def trade_order(file_old,file_new):
    with open(file_old) as file_old,open(file_new,"w",newline='') as file_new:
        reader_old=csv.DictReader(file_old)
        reader_new=csv.DictReader(file_new)
        fieldnames = ['first','last', 'house']
        writer_new=csv.DictWriter(file_new,fieldnames=fieldnames)
        writer_new.writeheader()
        for row in reader_old:
            new_last_name,new_name=row['name'].split(',')
            writer_new.writerow({'first':new_name .lstrip(),'last':new_last_name .lstrip(),'house':row['house']})

main()