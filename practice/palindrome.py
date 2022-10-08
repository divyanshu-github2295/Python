
def main():
    # Asking user input
    string = input("Enter something? ").lower().strip()
    # Calling palindrome_number function
    palindrome_number(string)


# Checking the string for palindrome
def palindrome_number(palindrome):
    count = 0
    for i in range(int((len(palindrome)+1)/2)):
        if palindrome[i] == palindrome[len(palindrome) - 1 - i]:
            count += 1
        else:
            print("Not Palindrome")
            break

    if count == int((len(palindrome)+1)/2):
        print("Palindrome")


if __name__ == "__main__":
    main()