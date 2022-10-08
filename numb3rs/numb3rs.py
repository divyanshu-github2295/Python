import re


def main():

    # Print the status of IP Address
    print(validate(input("IPV4 Address: ")))


# Checking IP Address
def validate(ip):

    flag = 0

    # list containing numbers (0-255)
    number = []
    for num in range(256):
        number.append(num)

    # Matching the ip address
    if re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        matches = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
        ip_tuple = matches.groups()
        print(ip_tuple)
        for match in ip_tuple:
            match = int(match)
            if match in number:
                flag += 1
            else:
                return False

        # Go inside when all digits in ip address in (0-255)
        if flag == 4:
            return True
    else:
        return False


if __name__ == "__main__":
    main()