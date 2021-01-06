#include <stdio.h>

int collatz(int n);

int main(void)
{
    int n = 7;
    int r = collatz(n);
    printf("collatz %i is: %i\n", n, r);
}

int collatz(int n)
{
    if (n == 1)
    {
        return 0;
    }
    else if (n % 2 == 0)
    {
        return 1 + collatz(n / 2);
    }
    else
    {
        return 1 + collatz(3*n + 1);
    }
}