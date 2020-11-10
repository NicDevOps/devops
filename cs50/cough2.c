// Abstraction

#include <stdio.h>

void cough();

int main()
{
    for (int i = 0; i < 3; i++)
    {
        cough();
    }
}

// Cough once
void cough()
{
    printf("cough\n");
}