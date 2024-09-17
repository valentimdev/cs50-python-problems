pergunta = input ("What is the Answer to the Great Question of Life, the Universe, and Everything?")              # type: ignore

def quarentadois():
    if checagem(pergunta):
        print("Yes")
    else:
        print("No")


def checagem(pergunta):
    pergunta=pergunta.strip()
    if(pergunta=="42" or pergunta.lower()=="forty-two" or pergunta.lower()=="forty two"):
        return True
quarentadois()
