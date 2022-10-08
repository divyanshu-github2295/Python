def main():

    string = text()
    bool = True
    bool = check(string)
    bool1 = True
    if bool == False:
        print(
            '''Either you enter Word or Number\nAlphanumeric contain both atleast one alphabet and one digit'''
        )
    else:
        bool1 = checkalnum(string)
        if bool1:
            print("Alphanumeric")


# user input
def text():
    return input().strip()

# checking for space and other characters other than alphabets and digits
def check(s):

    for i in s:
        if  not (i.isalpha() or i.isdigit()):
            return False


# checking alphanumeric
def checkalnum(s):

    alpha = []
    num = []

    for i in s:
        if i.isalpha():
            alpha.append(i)
        elif i.isdigit():
            num.append(i)


    if len(alpha) > 0 and len(num) > 0:
        return True
    elif len(alpha) == 0:
        return False
    elif len(num) == 0:
        return False


if __name__ == "__main__":
    main()

