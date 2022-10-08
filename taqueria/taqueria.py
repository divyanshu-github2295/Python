def main():

    # Restaurant Menu
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # calling order function
    order(menu)


# Caluculating bill of customser according to their order

def order(m):

    sum = 0
    while True:
        try:
            item = input("Item: ").title()
            if item in m:

                # Calculating bill
                sum = float(sum) + float(m[item])

                # Printing bill
                print(f"Total: ${sum:.2f}")

        except EOFError:
            print()
            break

        except KeyError:
            pass


main()
