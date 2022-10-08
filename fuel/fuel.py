# Fuel Gauge

def main():

    #calling get_fraction function
    x, y = get_fraction()

    #calling get_percentage function
    perc = get_percentage(x, y)

    #calling fuel_gauge function
    fuel_gauge(perc)


#Taking user input check value error and zero division error
def get_fraction():

    t = 0
    while True:
        try:
            fraction = input("Fraction: ")
            a, b = fraction.split("/")
            a = int(a)
            b = int(b)
            if a <= b:
                t = a / b
            else:
                continue

            break

        except (ValueError, ZeroDivisionError):        # for value error
            pass

    return a, b


# converting fraction to percentage value
def get_percentage(a, b):

    p = 0
    p = (a * 100) / b
    return int(p)


# Providing fuel details to user in percentage form
def fuel_gauge(p):

    if p <= 1:
        print("E")
    elif p == 99 or p == 100:
        print("F")
    else:
        print(str(p)+"%")


main()

