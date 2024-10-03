import random
import sys

def main():
    while True:
        level=input("Level: ")
        x=level.isnumeric()
        if x and int(level)>0:
            break
        else:
            continue
    level=int(level)
    if level>1:
        list_of_numbers = list(range(1,level))
    elif level==1:
        list_of_numbers = [1]
    number_choice=random.choice(list_of_numbers)
    guess(number_choice)
    sys.exit


def guess(number_choice):
        while True:
            guess=input("Guess: ")
            y=guess.isnumeric()
            if y==False:
                continue
            if int(guess)==number_choice:
                print("Just right!")
                break
            elif int(guess)>number_choice:
                print("Too large!")
            elif int(guess)<number_choice:
                print("Too small!")

main()
