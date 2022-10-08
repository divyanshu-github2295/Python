def main():

    # Prompting user for input
    tweet = input("Input: ")

    # Calling vowel removal function
    tweet = shorten(tweet)

    # Printing Result
    print("Output:", tweet)


# Removing vowel from input
def shorten(word):
    txt = []                  # Empty List

    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for c in word:
        if c in vowel:
            continue
        else:
            txt.append(c)

    word = "".join(txt)
    return word


if __name__ == "__main__":
    main()
