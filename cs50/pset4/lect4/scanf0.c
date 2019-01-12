// gets int from user using scanf

#include <stdio.h>

int main(void)
{
    int x;
    printf("x: ");
    scanf("%i", &x); // & = get the address of some variable
    printf("x: %i\n", x);
}