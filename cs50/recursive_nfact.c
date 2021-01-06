#include <stdio.h>

int fact(int n);

int main(void)
{
    int n = 4;
    int r = fact(n);
    printf("Factorial of %i is: %i\n", n, r);
}

int fact(int n)
{
    if (n == 1)
    {
        return 1;
    }
    else
    {
        return n * fact(n - 1);
    }
}