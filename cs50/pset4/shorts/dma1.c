// Dynamic Memory Allocation

#include <stdio.h>

int main(void)
{
  int m;  // lives on stack
  int * a;  // lives on stack

  int * b = malloc(sizeof(int));  // b lives on the stack, but the memory allocated to it lives on the heap. b is a pointer to this chunk of memory.

  a = &m;  // a now points to m the same way b points to memory allocated on the heap.

  a = b;  // a now points to what b points to. A DOES NOT POINT TO B!!
  // a = &b;  // this would be a pointing to b.

  m = 10;

  *b = m + 2;  // dereference b and put a value in that location

  free(b);  // free the memory allocated to b (the value of b disappears)

  *a = 11;  // oh dear god! what have you done!?
}
