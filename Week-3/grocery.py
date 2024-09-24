lista={}
frutas=[]
def main():
    fruta=input("")
    frutas.append(fruta)

while True:
    try:
        main()
    except:
        frutas.sort()
        for i in frutas:
            if i not in lista:
                lista[i]=1
            else:
                lista[i]+=1
        for i in lista.keys():
            print(lista[i],i.upper(),end="\n")
        break
