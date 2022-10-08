#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 0;
    do
    {
        n = get_int("Height: ");

    }
    while (n <= 0 || n>8);

    // for each row
    for (int i = 0; i<n; i++)
    {
        // for printing spaces in each column
        for(int j=0;j<((n-1)-i);j++)
        {
            printf(" ");
        }

        //for printing '#' in each column
        for(int k=0;k<=i;k++)
        {
            printf("#");
        }
        // for changing the row
        printf("\n");
    }
}