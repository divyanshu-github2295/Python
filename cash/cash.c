#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

// Asking and returning how many cents the customer owed
int get_cents(void)
{
    int x = 0;
    do
    {
        x = get_int("Changed owed: ");
    }
    while (x < 1);

    return x;
}

// Returning the calculated value number of quarters
int calculate_quarters(int cents)
{
    int q = 0;
    if (cents >= 25)
    {
        q = cents / 25;
    }
    return q;
}

// Returning the calculated value number of dimes
int calculate_dimes(int cents)
{
    int d = 0;
    if (cents >= 10)
    {
        d = cents / 10;
    }
    return d;
}

// Returning the calculated value number of nickels
int calculate_nickels(int cents)
{
    int n = 0;
    if (cents >= 5)
    {
        n = cents / 5;
    }
    return n;
}

// Returning the calculated value number of pennies
int calculate_pennies(int cents)
{
    int p = 0;
    p = cents / 1;
    return p;
}
