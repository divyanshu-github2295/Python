import inflect
import os


def main():

    # getting list of name
    name_list = get_names()

    # calling function for printing the message
    adieu_msg(name_list)


# Getting list of names
def get_names():
    list = []
    while True:
        try:
            list.append(input("Name: "))

        except EOFError:

            # Clearing the user input before printing the result
            os.system("clear")
            break

    return list


# print the Message
def adieu_msg(name):

    msg = inflect.engine()

    print(f"Adieu, adieu, to {msg.join(name)}")


if __name__ == "__main__":
    main()