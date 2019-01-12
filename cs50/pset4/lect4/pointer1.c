#include <stdio.h>

int main(void)
{
    int *ptr, q;
    q = 50;
    ptr = &q; // address of q is assigned to pointer
    printf("%d\n", *ptr); // display q's value using pointer
    return 0;
}