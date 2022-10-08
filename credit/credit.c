#include <cs50.h>
#include <stdio.h>

long card_number(void);
int count_length(long);
int check_sum(long, int);
int check_digits(long, int);
void check_platform(int, int, int);

int main(void)
{
    // Asking user to enter credit card number
    long num = card_number();
    // Counting digits in card number
    int count = count_length(num);
    // Checking starting digits of card
    int digits = check_digits(num, count);
    // Computing sum of digits according to luhn's Algorithm
    int sum = check_sum(num, count);
    // Checking cards Network
    check_platform(count, digits, sum);
}

//Returning credit card number entered by user
long card_number(void)
{
    long n = get_long("Card Number:");
    return n;
}

// Returning value count of digits in card number
int count_length(long n)
{
    int c = 0;
    while (n != 0)
    {
        n = n / 10;
        c++;
    }
    return c;
}

// Returning value of starting digits in card number
int check_digits(long n, int c)
{
    int j = 0;
    for (int i = 0; i < c - 2; i++)
    {
        j = n % 10;
        n = n / 10;
        if (n >= 40 && n <= 49)
        {
            n = n / 10;
        }
    }
    return n;
}

// Returning computed sum of digits according to luhn's Algorithm
int check_sum(long n, int c)
{
    long temp = n;
    int j = 0, sum = 0;

    int d = c / 2;

    if (c == 13 || c == 15)
    {
        d = (c / 2) + 1;
    }
    // start with last digit
    for (int i = 1; i <= d; i++)
    {
        j = temp % 10;
        sum = sum + j;
        temp = temp / 100;
    }
    temp = n / 10;
    // start with second-last digit
    for (int i = 1; i <= c / 2; i++)
    {
        j = temp % 10;
        temp = temp / 100;
        int s = 0, r = 0;
        s = j * 2;
        if (s >= 10 && s <= 18)
        {
            r = s % 10;
            sum = sum + r;
            s = s / 10;
            sum = sum + s;
        }
        else
        {
            sum = sum + s;
        }
    }
    return sum;
}

// Telling user about card's Network
void check_platform(int c, int d, int s)
{
    if (s % 10 == 0)
    {
        if ((d >= 51 && d <= 55) && c == 16)
        {
            printf("MASTERCARD\n");
        }
        else if ((d == 37 || d == 34) && c == 15)
        {
            printf("AMEX\n");
        }
        else if (d == 4 && (c == 13 || c == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}


