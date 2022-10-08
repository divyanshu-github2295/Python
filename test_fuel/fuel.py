def main():

    # Asking user for input
    frac = get_fraction()

    try:

        # calling get_fraction function
        perc = convert(frac)

        # calling fuel_gauge function
        value = gauge(perc)
        print(value)


    except (ValueError, ZeroDivisionError):
        pass



# Get Fraction
def get_fraction():

    return input("Fraction: ")


#Taking user input check value error and zero division error
def convert(fraction):

    x, y = fraction.split("/")

    if x.isalpha() or y.isalpha():
        raise ValueError

    elif y == "0":
        raise ZeroDivisionError

    else:

        if int(x) <= int(y):
            p_age = (int(x)/int(y))*100
            p_age = int(p_age)
            print(p_age)
            return p_age


# Providing fuel details to user in percentage form
def gauge(percentage):

    if percentage == 0 or percentage == 1:
        return "E"
    elif percentage == 99 or percentage == 100:
        return "F"
    elif percentage > 1:
        return (str(percentage)+"%")


if __name__ == "__main__":
    main()

