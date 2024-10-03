import random


def main():

    level = get_level()
    pontos = 0
    contador = 0
    while contador != 10:
        x, y = generate_integer(level), generate_integer(level)
        contador += 1
        tentativas = 0
        while tentativas != 3:
            try:
                respostas = int(input(f"{x} + {y} = "))
                if respostas != x + y:
                    if tentativas == 2:
                        print(f"{x} + {y} = {x+y}")
                        break
                    tentativas += 1
                    print("EEE")
                    continue
                else:
                    if tentativas == 0:
                        score += 1
                        break
                    break
            except ValueError:
                if tentativas == 2:
                    print(f"{x} + {y} = {x+y}")
                    break
                print("EEE")
                tentativas += 1
                continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):

    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()
