def main():
    saudacao = input("Greeting:")
    v=(value(saudacao))
    print(f"${v}")


def value(greeting):
    palavra = "hello"
    if palavra in greeting.lower():
        return 0
    elif greeting[0] == "h" or greeting[0] == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
