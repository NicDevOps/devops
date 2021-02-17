#include <stdio.h> // need for EXIT_SUCCESS constant
#include <stdlib.h> // need for printf

void increment_me (int *num) { *num += 1; }

int main (int argc, char **argv)
{
    // create a variable and a pointer to that variable
    int number = 10;
    int *p_number = &number;

    printf("number is %d and p_number dereference is %d\n", number, *p_number);
    // modify the value of the variable directly and via dereferencing
    increment_me(p_number);
    printf("number is %d and p_number dereference is %d\n", number, *p_number);
    // send the pointer and reference to a function and increment by 1
    increment_me(&number);
    printf("number is %d and p_number dereference is %d\n", number, *p_number);

    return EXIT_SUCCESS;
}

