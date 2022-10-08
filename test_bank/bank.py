def main():
    salutation = input("Greeting: ")
    money = value(salutation)
    print("$" + str(money))


# checking if right salutation is used
def value(greeting):

    greeting = greeting.lower().strip()
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()