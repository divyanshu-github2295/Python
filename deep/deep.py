def main():
    ans=input("What is the Answer to the Great Question of life, the Universe, and Everything? ")

   #strip(), for removing unnecessary spaces from strings
    check(ans.lower().strip())

# checking the string
def check(text):
    if text=="42" or text=="forty-two" or text=="forty two":
        print("Yes")
    else:
        print("No")

main()
