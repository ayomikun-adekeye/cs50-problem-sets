from pyfiglet import Figlet
figlet = Figlet()
import random
import sys

Fonts = figlet.getFonts()


def main():
    #no specs
    if len(sys.argv)==1:
        figlet.setFont(font= random.choice(Fonts))
        print(figlet.renderText(input("Input: ")))
    elif len(sys.argv)==3:
        try:
            if sys.argv[1]== '-f' or sys.argv[1]=='--font':
                figlet.setFont(font= sys.argv[2])
                print(figlet.renderText(input("Input: ")))
            else:
                sys.exit('Invalid usage')
        except:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')



main()
