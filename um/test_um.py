from um import count


def main():

    # Calling test_um_str function
    test_um_str()

    # Calling test_um_words function
    test_um_words()

    # Calling test_um_numbers function
    test_um_numbers()

    # Calling test_um_case function
    test_um_case()


# Testing if um.py can count "um" in text
def test_um_str():

    assert count("Hello, um ,world")
    assert count("um um")


# Testing whether programm ignoring the um in words
def test_um_words():

    assert count("Yummy") == 0
    assert count("circumference") == 0


# Testing whether programm ignoring the um in alphanumeric
def test_um_numbers():

    assert count("um123") == 0
    assert count("12um3") == 0


# Testing whether programm ignoring the case to count "um"
def test_um_case():

    assert count("Um")
    assert count("hello, UM, um")


if __name__ == "__main__":
    main()