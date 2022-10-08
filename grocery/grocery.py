# Program for making Grocery List

def main():

    # calling grocery function
    gro_list = grocery()
    
    #calling formating function
    formating(gro_list)


# Making grocery list
def grocery():
    dict = {}
    while True:
        try:
            fruit = input().strip()

            if fruit in dict:
                dict[fruit] = dict[fruit] + 1
            else:
                dict[fruit] = 1

        except EOFError:
            print()
            break

        except KeyError:
            pass

    return dict


# printing sorted grocery list
def formating(dict):
    for fruit in sorted(dict.keys()):
        print(dict[fruit], fruit.upper())


main()

