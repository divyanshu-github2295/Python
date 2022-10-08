import re


def main():

    # Calling count function and printing return value of count()
    print(count(input("Text:")))


# Finding the "um" in a string and returning the count
def count(s):
    count = 0

    # Returning tuple after finding "um" word
    tuple_um = re.findall(r"\bum\b", s, re.IGNORECASE)

    for value in tuple_um:
        if value.lower() == "um":
            count += 1

    return count


if __name__ == "__main__":
    main()