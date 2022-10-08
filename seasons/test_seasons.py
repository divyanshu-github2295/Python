from seasons import minute, in_words
import pytest


def main():

    # Calling test_input()
    test_input()

    # Calling test_minute()
    test_minute()

    # Calling test_in_words()
    test_in_words()


"""
minute() in seasons.py raise ValueError for invalid input handled using sys.exit()
: raise SystemExit Error : Because of sys.exit()
Atlast we look for SystemExit Error instead for ValueError
 """


# Testing for SystemExit Error
def test_input():

    with pytest.raises(SystemExit):
        assert minute("cat")
        assert minute("2022-11-35")


# Testing the calculation of minutes
def test_minute():

    assert minute("2021-06-09") == 525600
    assert minute("2022-06-08") == 1440


# Testing minutes are converting to proper string or not
def test_in_words():

    assert in_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert in_words(1051200) == "One million, fifty-one thousand, two hundred minutes"


if __name__ == "__main__":
    main()