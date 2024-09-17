prompt = input("Expression: ")
x,y,z=prompt.split(" ")
x=float(x)
z=float(z)
def operacoes(x,y,z):
    if y=="+":
        print("{:.1f}".format(float(x+z)))
    elif y=="-":
        print("{:.1f}".format(float(x-z)))
    elif y=="*":
        print("{:.1f}".format(float(x*z)))
    elif y=="/":
        print("{:.1f}".format(float(x/z)))
operacoes(x,y,z)