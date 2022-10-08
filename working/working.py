import re
import sys


def main():
    try:
        # Calling convert function and printing the result
        print(convert(input("Hours: ")))

    except ValueError:
        sys.exit("ValueError")


# Converting 12 hours format to 24 hours format
def convert(s):

    time = []

    # Checking the time format
    if re.search(r"^(\d{1}|1[0-2])(:[0-5][0-9])? ([AP]M) to (\d{1}|1[0-2])(:[0-5][0-9])? ([AP]M)$", s):
        match = re.fullmatch(r"^(\d{1}|1[0-2])(:[0-5][0-9])? ([AP]M) to (\d{1}|1[0-2])(:[0-5][0-9])? ([AP]M)$", s)

        # Adding value to time list
        for value in match.groups():
            if value != None:
                time.append(value)
            else:
                time.append(":00")

        # Convertion Process

        # Checking AM/PM for 1st time group
        if match.group(3) == "PM":

            if time[0] != "12":
                temp = int(time[0])
                temp += 12
                time[0] = str(temp)

            if match.group(6) == "PM":
                temp = int(time[3])
                temp += 12
                time[3] = str(temp)

            elif time[3] == "12":
                time[3] = "00"

            else:
                temp = int(time[3])
                time[3] = f"{temp:02}"

        # Checking AM/PM for 2nd time group
        elif match.group(6) == "PM":

            if time[3] != "12":
                temp = int(time[3])
                temp += 12
                time[3] = str(temp)

            if time[0] == "12":
                time[0] = "00"
            else:
                temp = int(time[0])
                time[0] = f"{temp:02}"

        else:
            # if both time are in AM
            if time[0] == "12":
                time[0] = "00"
            else:
                temp = int(time[0])
                time[0] = f"{temp:02}"

            if time[3] == "12":
                time[3] = "00"
            else:
                temp = int(time[3])
                time[3] = f"{temp:02}"

        return f"{time[0]}{time[1]} to {time[3]}{time[4]}"

    else:
        # Raising error time not in 12 hours format
        raise ValueError


if __name__ == "__main__":
    main()
    