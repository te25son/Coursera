// quick program to calculate how long it will take supporters of trumps wall
// to reach the goal of 5 billion dollars at the rate of making 2.3 million dollars
// every 3 days.

#include <stdio.h>

float getYears (float days);

int main (void)
{
    float days = 0;
    for (float amount = 0; amount < 5000; amount += 0.83)
    {
        days ++;
    }

    float years = getYears(days);
    printf("%.2f years\n", years);
}

float getYears (float days)
{
    return days / 365;
}