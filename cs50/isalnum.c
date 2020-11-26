/* Example using isalnum by TechOnTheNet.com */

#include <stdio.h>
#include <ctype.h>

int main(int argc, const char * argv[])
{
    /* Define a temporary variable */
    unsigned char test;

    /* Assign a test letter to the variable */
    test = 'T';

    /* Test to see if this character is alphanumeric */
    if (isalnum(test) != 0) printf("%c is alphanumeric\n", test);
    else printf("%c is not alphanumeric\n", test);

    /* Assign a non-alphanumeric character to the variable */
    test = '!';

    /* Test to see if this character is alphanumberic */
    if (isalnum(test) != 0) printf("%c is alphanumeric\n", test);
    else printf("%c is not alphanumeric\n", test);

    return 0;
}