import sys


def main():

    # calling check_command_line function
    check_command_line()

    # calling count_line function returning count
    count = count_line()
    print(count)


# Checking command-line argument entered by user
def check_command_line():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
        
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")



# Counting lines in program
def count_line():

    line = 0
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        blank = []
        for string in lines:

            # storing lines in form of list in blank list
            blank = string.split()

            # Removing spaces to left of string
            string = string.lstrip()

            if string.startswith("#"):
                continue
            elif blank == []:
                continue
            else:
                line += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    return line


if __name__ == "__main__":
    main()
