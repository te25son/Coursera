// basic examples of how pointers work

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // allocate two pointers x, y
    int* x;
    int* y;

    // initially pointers don't point to anything
    // you must set up "appointees" as a separate step

    // set up a pointee by allocating memory and point x to it
    x = malloc(sizeof(int));

    // dereference the pointer x to store 42 in the pointee
    *x = 42;

    // set pointer y to point at pointer x
    y = x;

    // deference the pointer y to store 13 in the pointee
    *y = 13;

    printf("x: %i\n", *x);
    printf("y: %i\n", *y);
}