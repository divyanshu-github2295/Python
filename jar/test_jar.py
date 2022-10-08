import pytest
from jar import Jar


# Testing Initialization of Capacity
def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    jar = Jar(9)
    assert jar.capacity == 9


# Testing for Value Error raised if user input is Negative
def test_init_raise_valueError():
    with pytest.raises(ValueError, match="Capacity cannot be negative"):
        jar = Jar(-5)
        jar = Jar(-15)


# Testing whether str function returning numnber of cookies in jar
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# Testing whether deposit function working properly or not
def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6


# Testing for Value Error raised when Capacity is exceed
def test_deposit_Value_Error():
    with pytest.raises(ValueError, match="Exceed Capacity"):
        jar = Jar(6)
        jar.deposit(7)


# Testing whether withdraw function working properly or not
def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3


# Testing for Value Error raised when jar not have sufficient cookies to withdraw
def test_withdraw_Value_Error():
    with pytest.raises(ValueError, match="Not Enough Cookie's"):
        jar = Jar(15)
        jar.deposit(12)
        jar.withdraw(13)
