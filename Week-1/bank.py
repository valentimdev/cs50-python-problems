def main():
    saudacao = input("Greeting:")
    print(checagem(saudacao))
    

def checagem(saudacao):
    palavra = "hello"
    if palavra in saudacao.lower():
        return "$0"
    elif saudacao[0]=="h" or saudacao[0]=="H":
        return "$20"
    else:
        return "$100"

main()