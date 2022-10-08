import random


def main():

    guess_number(get_level())


# Getting User Level
def get_level():
    while True:
        try:
            n = int(input("Level: "))

            # Ensuring level entered is positive integer
            if n > 0:
                return n
        except ValueError:
            continue


# Guessing game asking user for guess
def guess_number(n):

    # Generating random number according to level
    num = random.randint(1, n)


# Asking user to guess the number
    while True:
        try:
            guess = int(input("Guess: "))

            # Ensuring number entered is positive integer
            if guess > 0:
                if num > guess:
                    print("Too small!")
                    continue
                elif num < guess:
                    print("Too large!")
                    continue
                else:
                    print("Just right!")
                    break
        except ValueError:
            continue


if __name__ == "__main__":
    main()

