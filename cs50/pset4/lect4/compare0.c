#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("s: ");
    string t = get_string("t: ");

    if (s == t)
    {
        printf("SAME\n");
    }
    else
    {
        printf("DIFF\n");
    }
}