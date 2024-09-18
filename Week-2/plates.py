def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(p):
    if(p[round(len(p)/2)] != '0'):
        if len(p)>=2 and len(p)<=6:
            if(p.isalpha()):return True
            for i in range(len(p)):
                if i<=(len(p)/2) and p[i].isalpha():
                    continue
                elif (i>=(len(p)/2)) and p[i].isnumeric():
                    continue
                else :
                    return False
                    break
            return True
    else:return False
    

main()
