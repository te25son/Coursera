#include <stdio.h>

void fun(int *ptr) // takes an ADDRESS as its parameter
{
  *ptr = 30; // * is a dereference operator. Therefore, *ptr dereferences the value at that address and reassigns the value to, in this case, 30.
}

int main()
{
  int y = 20; // sets variable y to equal 20
  fun(&y); // assigns the ADDRESS of y to the function fun
  printf("%d\n", y);
  return 0;
}
