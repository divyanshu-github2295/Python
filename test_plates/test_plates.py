from plates import is_valid


def main():

    # test for length
    test_length()

    # test for starting 2 letters
    test_start_2()

    # test for alphabets after starting 2
    test_last_alpha()

    # test first occurring digit
    test_first_digit()

    # test for digits after first occuring digit
    test_last_digits()

    # test for space and any punctuation not present in plate number
    test_alphanumeric()


# test for length
def test_length():
    assert is_valid("cs50") == True
    assert is_valid("dv") == True
    assert is_valid("v") == False
    assert is_valid("cs5555f") == False
    assert is_valid("Helloman") == False


# test for starting 2 letters
def test_start_2():
    assert is_valid("Hello") == True
    assert is_valid("h145") == False


# test for alphabets after starting 2
def test_last_alpha():
    assert is_valid("cspython") == False
    assert is_valid("python") == True


# test first occurring digit
def test_first_digit():
    assert is_valid("te0401") == False
    assert is_valid("te4510") == True


# test for last digits
def test_last_digits():
    assert is_valid("ca14tp") == False
    assert is_valid("ca1452") == True


# test for space and any punctuation not present in plate number
def test_alphanumeric():
    assert is_valid("cd 40") == False
    assert is_valid("cd?40") == False
    assert is_valid("test50") == True


if __name__ == "__main__":
    main()