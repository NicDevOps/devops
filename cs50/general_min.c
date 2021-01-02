#include <stdio.h>

#define ARRAY_SIZE 5

int min(int array[], int size)
{
    int min = array[0];

    for (int i = 0; i < size; i++)
    {
        if (array[i] < min)
        {
            min = array[i];
        }
    }
    
    return min;
}

int main ()
{
    int array[ARRAY_SIZE] = {34, 5, 12, 9, 1};
    int result = min(array, ARRAY_SIZE);
    printf("%i\n", result);
}
