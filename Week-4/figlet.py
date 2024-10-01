import sys
import random
from pyfiglet import Figlet
def main():
    figlet = Figlet()
    random.seed()
    fonte=figlet.getFonts()
    if checagem(figlet):
        sys.exit("Invalid usage")
    texto=input("Input: ")
    if len(sys.argv)==1:
        figlet.setFont(font=random.choice(fonte))
        print(figlet.renderText(texto))
    elif len(sys.argv)==3:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(texto))
def checagem(figlet):
        if len(sys.argv)==2  or len(sys.argv)>3:
            return True
        try:
            if sys.argv[2] not in figlet.getFonts() or sys.argv[1]!="-f" and sys.argv[1]!="--font":
                return True
            
        except:
            return False

main()