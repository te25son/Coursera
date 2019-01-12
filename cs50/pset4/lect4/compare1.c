#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    char * s = get_string("s: ");
    char * t = get_string("t: ");

    int res = strcmp(s, t);

    if (res == 0)
    {
        printf("SAME\n");
        printf("%i\n", res);
    }
    else
    {
        printf("DIFF\n");
        printf("%i\n", res);
    }
}