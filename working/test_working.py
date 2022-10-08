import pytest
from working import convert


def main():

    # Calling test_valid_input function
    test_valid_input()

    # Calling test_invalid_input function
    test_invalid_input()

    # Calling test_invalid_time function
    test_invalid_time()


# Checking Valid input giving proper output
def test_valid_input():

    assert convert("11 AM to 5 PM") == "11:00 to 17:00"
    assert convert("10:30 PM to 12 AM") == "22:30 to 00:00"


# Checking programme raises a Value Error with invalid input
def test_invalid_input():

    with pytest.raises(ValueError):
        assert convert("cat")
        assert convert("123hi")


# Checking programme raises a Value Error with Invalid Time
def test_invalid_time():

    with pytest.raises(ValueError):
        assert convert("11:60 PM to 6 PM")
        assert convert("9:60 AM to 5:67 PM")


if __name__ == "__main__":
    main()