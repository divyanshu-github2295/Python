import sys
import csv


def main():
    mydict = {}

    # Calling check_command_line function
    check_command_line()

    # Calling read_csv function and returning list
    mydict = read_csv()

    # Calling write_csv function
    write_csv(mydict)


# Checking command-line arguments
def check_command_line():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


# Reading csv file
def read_csv():
    dict = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                dict.append({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    return dict


# Writing csv file
def write_csv(dict):

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for write in dict:
            writer.writerow({"first": write["first"], "last": write["last"], "house": write["house"]})


if __name__ == "__main__":
    main()
