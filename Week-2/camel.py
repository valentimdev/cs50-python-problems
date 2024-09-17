palavra=input("camelCase: ")
def main(palavra):
    nova_palavra=""
    for i in range(len(palavra)):
        if(palavra[i].isupper()):
            nova_palavra+="_"+(palavra[i].lower())
        else:
            nova_palavra+=palavra[i]
    print("snake_case: "+nova_palavra)

main(palavra)
