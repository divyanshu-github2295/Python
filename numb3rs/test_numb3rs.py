from numb3rs import validate


def main():

    # Calling test function
    test_valid_ip_address()
    test_invalid_ip_address()


# Testing valid ip address
def test_valid_ip_address():

    assert validate("1.2.3.4") == True
    assert validate("255.255.255.0") == True


# Testing invalid ip address
def test_invalid_ip_address():

    assert validate("22.54.267.25") == False
    assert validate("cat") == False


if __name__ == "__main__":
    main()
