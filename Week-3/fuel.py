def main():
    valor=input("Fraction: ")
    x,y=(valor.split("/"))
    x=int(x)
    y=int(y)
    final=(x/y)*100
    if(final>100):
        main()
    if(final>=99):
        print("F")
    elif(final<=1):
        print("E")
    else:
        print(f"{round(final)}%")

while True:
    try:
        main()
        break
    except (ValueError,ZeroDivisionError):
        pass