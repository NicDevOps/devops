/* Example using isalpha by TechOnTheNet.com */

#include <stdio.h>
#include <ctype.h>

int main(int argc, const char * argv[])
{
    /* Define a temporary variable */
    unsigned char test;

    /* Assign a test letter to the variable */
    test = 'T';

    /* Test to see if this is a alphabet character */
    if (isalpha(test) != 0) printf("%c is in the alphabet\n", test);
    else printf("%c is not in the alphabet\n", test);

    /* Assign a non-alphabetic character to the variable */
    test = '7';

    /* Test to see if this is a alphabet character */
    if (isalpha(test) != 0) printf("%c is in the alphabet\n", test);
    else printf("%c is not in the alphabet\n", test);

    return 0;
}