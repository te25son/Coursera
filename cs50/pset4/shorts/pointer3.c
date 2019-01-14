// dereferencing a pointer

#include <stdio.h>

int main()
{
  int x, y;  // set up to vars x and y
  int * ptr;  // set up pointer that points to an int

  x = 10;  // set value of x to 10
  prt = &x;  // point the pointer to the address of x

  print("%i\n", *ptr);  // print the value of x using the pointer

  y = *ptr;  // dereference the pointer and assign y to it

  printf("%i\n", y);  // print the value of y

  return 0; 
}
