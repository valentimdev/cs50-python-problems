import inflect
lista_nomes=[]
p=inflect.engine()
def main():
    nome=input("Name: ")
    lista_nomes.append(nome)
while True:
    try:
        main()
    except:
        break
print("Adieu, adieu, to ",end="")
print(p.join(lista_nomes))
