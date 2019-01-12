// program to calculate how long (in years) it will take to save x amount of dollars
// while putting away x amount / day into savings

#include <stdio.h>
#include <cs50.h>

float get_years(int days);

int main (void)
{
    // define global variables
    float goal, days_saving, saved = 0;
    int days = 0;

    // get the goal to be saved from user
    do
    {
        goal = get_float("Total amount to be saved in dollars: ");
    }
    while(goal <= 0);

    // get the amount saved / day from user
    do
    {
        days_saving = get_float("Total amount to be saved / day in dollars: ");
    }
    while(days_saving <= 0);

    // calculate the number of days it will take to reach goal
    while (saved < goal)
    {
        saved+=days_saving;
        days++;
    }

    // convert days to years
    float years = get_years(days);

    // print the total time (in days and years) it will take to reach goal
    printf("It will take %i days (or %.2f years) to reach your goal of $%.2f while saving $%.2f per day.\n", days, years, goal, days_saving);
}

float get_years(int days)
{
    return days / 365;
}