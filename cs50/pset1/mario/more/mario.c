#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int rows, htags, spaces;

    // prompt user for number of rows
    // must be a positive number no larger than 23
    do
    {
        rows = get_int("Postive number: ");
    }
    while(rows < 0 || rows > 23);

    // set starting points for htags and spaces
    htags = 1;
    spaces = rows - 1;

    // build the steps
    for(int i = 0; i < rows; i++)
    {
        // left-hand steps
        // print spaces
        for(int j = 0; j < spaces; j++)
        {
            printf(" ");
        }
        spaces--;

        //print hashtags
        for(int k = 0; k < htags; k++)
        {
            printf("#");
        }

        // gap
        printf("  ");

        //right-hand steps
        for(int l = 0; l < htags; l++)
        {
            printf("#");
        }
        htags++;

        printf("\n");
    }
}