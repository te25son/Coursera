#include <stdio.h>

int main(void)
{
  int* pk;
  int k = 35;
  pk = &k;

  printf("%i\n", *pk);

  int m = 4;
  pk= &m;
  printf("%i\n", *pk);
}
