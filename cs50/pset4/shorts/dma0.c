// dynamically allocated memory

#include <stdio.h>

int main(void)
{
  // statically obtain an integer
  // this integer lives on the stack
  int y;

  // dynamically obtain an integer
  // this integer lives on the heap
  int * ptr = malloc(sizeof(int));

  // get an integer from the user
  int x = GetInt();

  // array of floats on the stack
  float stack_array[x];

  // array of floats on the stack
  float * heap_array malloc(x * sizeof(float));

  char * word = malloc(50 * sizeof(char));

  // do stuff with word

  // free the memory for word so you don't get memory leaks
  free(word);

  // IMPORTANT:
  // All memory you malloc() must be freed when you're done using it!
  free(ptr);
  free(heap_array);
}
