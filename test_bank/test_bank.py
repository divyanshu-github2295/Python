from bank import value


def main():

    # Calling test_value function
    test_hello()

    # Calling test_start_h function
    test_start_h()

    # Calling test_other function
    test_other()


# Test for "hello"
def test_hello():

    assert value("Hello") == 0
    assert value("Hello, Charlie") == 0
    assert value("hello, goodbye") == 0
    assert value("hello, good") == 0


# Test for word start with "h"
def test_start_h():

    assert value("How you doin'") == 20
    assert value("Hey, joey") == 20


# test for other word
def test_other():

    assert value("whats happening") == 100
    assert value("Good Morning!") == 100


if __name__ == "__main__":
    main()