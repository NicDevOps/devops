// http://valgrind.org/docs/manual/quick-start.html#quick-start.prepare

#include <stdlib.h>
#include <stdio.h>

void f(void)
{
    int *x = malloc(10 * sizeof(int));
    *(x+8) = 3;
    x[9] = 5;
    printf("%p\n", &x[9]);
    printf("%p\n", &*(x+9));
    free(x);
}

int main(void)
{
    f();
    return 0;
}