def main():
    salutation=input("Greeting: ").lower().strip()
    checking(salutation)

#checking if right salutation is used
def checking(greet):
    if greet.startswith("h"):
        if greet.startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()