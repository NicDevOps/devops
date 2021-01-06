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
    int product = 1;

    while (n > 0)
    {
        product *= n;
        n--;
    }

    return product;
}