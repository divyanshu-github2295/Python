import sys
import random
from pyfiglet import Figlet


def main():

    text = get_input()
    styling(text)


# Getting Input from User
def get_input():
    figlet = Figlet()
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet.getFonts():
                return input("Input: ")
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    except IndexError:
        sys.exit("Invalid Usage")


# styling given text into FIGlet
def styling(t):
    figlet = Figlet()

    # Getting fonts from figlet module
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:

        # Setting the font and randomly choicing font
        figlet.setFont(font=random.choice(fonts))

        # printing text in FIGlet format
        print(figlet.renderText(t))

    elif len(sys.argv) == 3:

        # Setting the font provided by user
        figlet.setFont(font=sys.argv[2])

        # printing text in FIGlet format
        print(figlet.renderText(t))


if __name__ == "__main__":
    main()
