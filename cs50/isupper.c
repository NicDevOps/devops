#include <stdio.h>
#include <ctype.h>

int main(int argc, const char * argv[])
{
    /* Define a variable to hold our test letter */
    int letter;

    /* Set the letter to a uppercase 'A' */
    letter = 'A';

    /* Test to see if the letter provided is uppercase */
    if (isupper(letter)) printf("'%c' is uppercase\n", letter);
    else printf("'%c' is lowercase\n", letter);

    /* Set the letter to a uppercase 'a' */
    letter = 'a';

    /* Test to see if the letter provided is uppercase */
    if (isupper(letter)) printf("'%c' is uppercase\n", letter);
    else printf("'%c' is lowercase\n", letter);

    return 0;
}