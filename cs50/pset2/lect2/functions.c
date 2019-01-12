#include <stdio.h>
#include <cs50.h>

// float multiTwoFloats(float a, float b)
// {
//     // float product = a * b;
//     // return product;

//     // OR SIMPLY...

//     return a * b;
// }

// int add_two_ints(int a, int b)
// {
//     return a + b;
// }

bool valid_triangle(int a, int b, int c);

int main(void)
{
    int side1 = 0, side2 = 0, side3 = 0;
    string name = get_string("Give me a name for your triangle: ");
    // get side 1 if side 1 is > 0
    do
    {
        side1 = get_int("Give me the first side of a triangle: ");
    }
    while(side1 <= 0);

    // get side 2 if side 2 is > 0
    do
    {
        side2 = get_int("Give me the second side of a triangle: ");
    }
    while(side2 <= 0);

    // get side 3 if side 3 is > 0
    do
    {
        side3 = get_int("Give me the third side of a triangle: ");
    }
    while(side3 <= 0);

    if (valid_triangle(side1, side2, side3))
    {
        printf("%s is a valid triangle!\n", name);
    }
    else
    {
        printf("%s is NOT a valid triangle :(\n", name);
    }
}

bool valid_triangle(int a, int b, int c)
{
    if (a+b>c && a+c>b && b+c>a)
    {
        return true;
    }
    else
    {
        return false;
    }
}