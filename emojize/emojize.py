import emoji


def main():

    # calling input function
    emo = get_emoji()
    # calling print fuction
    print_emoji(emo)


# getting user input

def get_emoji():
    return input("Input: ")


# printing user input in emoji form

def print_emoji(em):
    print(emoji.emojize(f"Output: {em}", language='alias'))


main()
