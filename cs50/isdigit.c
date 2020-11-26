/* Example using isdigit by TechOnTheNet.com */

#include <stdio.h>
#include <ctype.h>

int main(int argc, const char * argv[])
{
    /* Define a temporary variable */
    unsigned char test;

    /* Assign a test decimal digit character to the variable */
    test = '7';

    /* Test to see if this is a decimal digit character */
    if (isdigit(test) != 0) printf("%c is a decimal digit character\n", test);
    else printf("%c is not a decimal digit character\n", test);

    /* Assign a non-digit character to the variable */
    test = 'T';

    /* Test to see if this is a decimal digit character */
    if (isdigit(test) != 0) printf("%c is a decimal digit character\n", test);
    else printf("%c is not a decimal digit character\n", test);

    return 0;
}