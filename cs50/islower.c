/* Example using islower by TechOnTheNet.com */

#include <stdio.h>
#include <ctype.h>

int main(int argc, const char * argv[])
{
    /* Define a variable to hold our test letter */
    int letter;

    /* Set the letter to a lowercase 'b' */
    letter = 'b';

    /* Test to see if the letter provided is lowercase */
    if (islower(letter)) printf("'%c' is lowercase\n", letter);
    else printf("'%c' is uppercase\n", letter);

    /* Set the letter to a uppercase 'B' */
    letter = 'B';

    /* Test to see if the letter provided is lowercase */
    if (islower(letter)) printf("'%c' is lowercase\n", letter);
    else printf("'%c' is uppercase\n", letter);

    return 0;
}