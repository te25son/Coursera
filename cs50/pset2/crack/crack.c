#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // check that two arguments are given
    if (argc == 2)
    {
        printf("%s\n", argv[1]);
    }
    else
    {
        printf("ERROR\n");
        return 1;
    }
}