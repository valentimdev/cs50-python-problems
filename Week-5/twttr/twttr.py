def main():
    word=input("Input: ")
    print(shorten(word))



def shorten(word:str):
    newname = ""
    for i in word:
        if i in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            continue
        else:
            newname += i
    return newname


if __name__ == "__main__":
    main()
