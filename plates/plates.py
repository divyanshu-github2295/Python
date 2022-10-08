def main():
    plate = input("Plate: ").upper().strip()

    # Checking the validity of Plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    c = len(s)                      # Length of number plate
    i = 0

    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]         # Digits list

    if s.isalnum():
        if not(c > 1 and c < 7):      # For confirm length of plate
            return False
        if not s[:2].isalpha():         # For confirm first two letter of plate
            return False
        if c > 2:
            if not s[2:].isalpha():         # For confirm the last letters are alphabets or not
                for n in s[2:]:
                    if n in digits:
                        if n == "0":        # For confirm first digit if "0" return false
                            return False
                        else:
                            i = s.index(n)  # Indexing the first digit occured
                    else:
                        continue

                    if s[i:].isdigit():     # For confirm digits after first digit
                        return True
                    else:
                        return False
            else:
                return True
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()

