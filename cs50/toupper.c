/* Example using tolower by TechOnTheNet.com */

#include <stdio.h>
#include <ctype.h>

int main(int argc, const char * argv[])
{
    /* Define a variable and set it to 'A' */
    int letter = 'A';

    /* Display a lowercase 'A' */
    printf("Lowercase '%c' is '%c'\n", letter, tolower(letter));

    return 0;
}