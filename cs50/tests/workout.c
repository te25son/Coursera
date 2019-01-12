// program that builds a workout plan for a week

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // set global variables
    int max_weight = 0, ramped[5];
    float percent = 0.6;

    // get the weight from the user
    do
    {
        max_weight = get_int("Enter max weight: ");
    }
    while(max_weight <= 0);

    //
    for (int i = 0; i < 5; i++)
    {
        int num = (max_weight * percent);
        int mod = num % 5;

        ramped[i] = (max_weight * percent) - mod;

        if (i < 2)
        {
            percent += 0.2;
        }

        if (mod > 0)
        {
            ramped[i] += 5;
        }

        printf("Set %i : %i\n", i + 1, ramped[i]);
    }
}