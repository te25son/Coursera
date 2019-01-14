// example from:
// https://doc.lagout.org/programmation/C/Understanding%20and%20Using%20C%20Pointers%20%5BReese%202013-05-18%5D.pdf

#include <stdio.h>

int main()
{
  char *names[] = {"Miller", "Jones", "Anders"};
  printf("%c\n", *(*(names + 1) + 2));
  printf("%c\n", names[1][2]);
  return 0;
}
