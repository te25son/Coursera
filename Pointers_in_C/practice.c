# include <stdio.h>

int main()
{
  // define variable a
  int a = 1;

  // define pointer variable pointer_to_a and point to a using the & symbol
  int * pointer_to_a = &a;

  // change the variable
  a += 1;

  // change the pointer variable
  *pointer_to_a += 1;

  // print a
  printf("The value of a is %d\n", a);  // 3
}
