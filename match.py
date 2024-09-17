name = input("What's your name?").capitalize()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        print("Who?")