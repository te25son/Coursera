// dangerously gets a string from user using scanf

#include <stdio.h>

int main(void)
{
    char s[5];  // set asside amount of memory you wish to use. itc 5
    printf("s: ");  // prompt the user for a string
    scanf("%s", s);  // scan the users input to the location of s
    printf("s: %s\n", s);  // print s
}