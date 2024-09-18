name=input("Input: ")

def main():
    newname=''
    for i in name:
        if i in ["a","A","e","E","i","I","o","O","u","U"]:
            continue
        else:
            newname+=i
    print(newname)
main()
