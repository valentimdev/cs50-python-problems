saudacao = input("Greeting:")
palavra = "hello"

def checagem(saudacao):
    if palavra in saudacao.lower():
        print("$0")
    elif saudacao[0]=="h" or saudacao[0]=="H":
        print("$20")
    else:
        print("$100")

checagem(saudacao)
