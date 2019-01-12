#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    // get a string
    char * s = get_string("s: ");

    // make sure s is actually a string
    if (!s)
    {
        return 1;
    }

    // allocate memory for another string
    // malloc = Memory ALLOCation
    char * t = malloc((strlen(s) + 1) * sizeof(char));

    // make sure t is actually a string
    if (!t)
    {
        return 1;
    }

    // copy string into allocated memory
    for (int i = 0; i <= strlen(s); i++)
    {
        t[i] = s[i];
    }

    // capitalize first letter in copy
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // print string
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}