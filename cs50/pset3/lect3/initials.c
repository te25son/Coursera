#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // get user input name
    string name = get_string("Name: ");

    // define an array containing chars
    char initials[4];  // first, middle, last, null [4]

    // get counter for array
    int counter = 0;

    // iterate over characters in name
    for (int i = 0; i < strlen(name); i++)
    {
        // if upper case letter, add to initials array
        if (isupper(name[i]))
        {
            initials[counter] = name[i];
            counter ++;
        }
    }

    // intsert null at the end of array
    initials[counter] = '\0';
    printf("%s\n", initials);
}
