import pytest
from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()
    test_ValueError()
    test_ZeroDivisionError()


# Testing convertion function
def test_convert():

    assert convert("1/4")
    assert convert("2/3")


# Testing percentage value
def test_gauge():
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"


# testing for value error raised by convert function
def test_ValueError():
    with pytest.raises(ValueError):
        assert convert("cat/dog")


# testing for zero division error raised by convert function
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")


if __name__ == "__main__":
    main()