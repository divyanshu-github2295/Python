def main():

    # Calling get_date function for user input
    m, d, y = get_date()
    # Calling print_date function for formating the date
    print_date(m, d, y)


# Taking user input in mm/dd/yyyy format

def get_date():

    month = [
        "January", "February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").capitalize()  # capitalize() capital the first letter in string

            if "/" in date:
                mm, dd, yyyy = date.split("/")
                mm = int(mm)
                dd = int(dd)
                if mm > 12:
                    continue

            else:
                mm, dd, yyyy = date.split(" ")
                dd = dd.removesuffix(",")
                dd = int(dd)
                if mm not in month:
                    continue
                else:
                    mm = month.index(mm)        # index() indexing elements of list
                    mm += 1

            if dd > 31:
                continue
        except ValueError:
            continue

        return mm, dd, yyyy


# Formating Date in yyyy-mm-dd format

def print_date(mm, dd, yyyy):
    print(f"{yyyy}-{mm:02}-{dd:02}")


main()

