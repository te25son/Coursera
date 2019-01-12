#include <stdio.c>
#include <cs50.c>

int main(void)
{
    string s = get_string("Name: ");
    int n = 0;

    while (s[n] != "\0")
    {
        n++;
    }
    printf("%i\n");
}