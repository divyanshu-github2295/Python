import sys
import csv
from tabulate import tabulate


def main():

    # Calling check_command_line function
    check_command_line()

    # Calling read_file function and getting list of pizza
    pizza_list = read_file()

    # Printing list in formatted table
    print(tabulate(pizza_list, headers="firstrow", tablefmt="grid"))


# Checking command-line argument
def check_command_line():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line argument")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a csv file")


# Reading csv file and returning it in list format
def read_file():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            pizzza = []
            for row in reader:
                pizzza.append([row[0], row[1], row[2]])

        return pizzza

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()