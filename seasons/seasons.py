import re
import sys
import inflect
from datetime import date


def main():

    # Input in YYYY-MM-DD Format
    dat = input("Date of Birth: ")
    
    # Calling minute(), passing DOB and getting minutes between respected dates
    total_min = minute(dat)

    # Calling in_words function
    print(in_words(total_min))


# Checking User Input in YYYY-MM-DD format
def minute(dob):

    # Getting todays date
    today = date.today()

    try:

        # Verifying date format
        if re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", dob):
            year, mm, dd = dob.split("-")
            dob = date(int(year), int(mm), int(dd))
            num_days = abs(dob - today)

            min = num_days.days * 24 * 60

            return min

        else:
            raise ValueError

    except ValueError:
        sys.exit("Invalid date")


# Printing minutes in number to words
def in_words(minutes):

    word = inflect.engine()
    words = word.number_to_words(minutes, andword="")
    result = words.capitalize() + " minutes"
    return result


if __name__ == "__main__":
    main()