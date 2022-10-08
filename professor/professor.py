from random import randint


def main():

    # Getting User level
    lvl = get_level()

    try:

        # Getting generated integers
        first, second = generate_integer(lvl)
        score = 0
        # Storing correct answer
        for i in range(10):
            error = 0
            answer = first[i] + second[i]
            answer = str(answer)

            while True:
                print(f"{first[i]} + {second[i]} = ", end="")
                ans = input()

                # Checking user answer and counting error made by user
                if ans != answer and error < 3:
                    print("EEE")
                    if error == 2:
                        print(f"{first[i]} + {second[i]} =", answer)
                        break
                    error += 1
                    continue
                elif ans == answer:
                    score += 1
                    break
                else:
                    break

        # Printing user score
        print("Score:", score)

    except ValueError:
        pass


# Asking User for Level
def get_level():
    while True:
        try:
            L = int(input("Level: "))
            if 0 < L <= 3:
                return L

        except ValueError:
            continue


# Generating random integer for questions
def generate_integer(level):

    first = []
    second = []
    if level == 1:

        # Making questions according to level
        for i in range(10):
            first.append(randint(0, 9))
            second.append(randint(0, 9))

    elif level == 2:

        # Making questions according to level
        for i in range(10):
            first.append(randint(10, 99))
            second.append(randint(10, 99))

    elif level == 3:

        # Making questions according to level
        for i in range(10):
            first.append(randint(100, 999))
            second.append(randint(100, 999))

    else:
        raise ValueError

    return first, second


if __name__ == "__main__":
    main()
