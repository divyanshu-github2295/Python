def main():
    num = input("Enter Number(1-9999): ")
    number_words(num)


# Convertion Table for Numbers to words
def convertion_table():
    mydict = {10: "Ten", 1000: "Thousand", 11: "Eleven",
            1: "One", 100: "Hundred", 12: "Twelve",
            2: "Two", 20: "Twenty", 13: "Thirteen",
            3: "Three", 30: "Thirty", 14: "Fourteen",
            4: "Four", 40: "Forty", 15: "Fifteen",
            5: "Five", 50: "Fifty", 16: "Sixteen",
            6: "Six", 60: "Sixty", 17: "Seventeen",
            7: "Seven", 70: "Seventy", 18: "Eighteen",
            8: "Eight", 80: "Eighty", 19: "Nineteen",
            9: "Nine", 90: "Ninety"
        }
    tens = ["11", "12", "13", "14", "15", "16", "17", "18", "19"]
    return mydict, tens


# Doing Convertion
def number_words(number):

    number = list(number)
    places = []

    mydict, tens = convertion_table()

    # Getting the Places(One's , Ten's, Hundred's and so on...)
    for i in range(len(number)):
        temp = int(number[i])
        if temp != 0:
            power = pow(10, len(number) - 1 - i)
            places.append(power)
        else:
            places.append(0)

    # Convertion Process number to words
    if number[len(number) - 2] == "1":
        number[len(number) - 2] = number[len(number) - 2] + number[len(number) - 1]
        number.pop(len(number) - 1)
        places.pop(len(number) - 1)

    for i in range(len(places)):
        if number[i] in tens:
            print(mydict[int(number[i])])
        elif places[i] == 10 or places[i] == 1:
            print(mydict[int(number[i]) * places[i]], end=" ")
        elif int(number[i]) in mydict:
            print(mydict[int(number[i])], end=" ")
            print(mydict[places[i]], end=" ")

    print()


if __name__ == "__main__":
    main()

