#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float input;
    do
    {
        input = get_float("Change due: ");
    }
    while(input < 0);

    // constant variables
    float total = 0.00;
    int coins = 0;

    while(total < input)
    {
        // coins
        float quarter = 0.25;
        float dime = 0.10;
        float nickle = 0.05;
        float penny = 0.01;

        // logic
        // start biggest and go smallest
        if((total + quarter) <= input)
        {
            total += quarter;
            coins ++;
        }
        else if((total + dime) <= input)
        {
            total += dime;
            coins ++;
        }
        else if((total + nickle) <= input)
        {
            total += nickle;
            coins ++;
        }
        else
        {
            total += penny;
            coins ++;
        }
    }

    // print final total of coins
    printf("%i\n", coins);
}