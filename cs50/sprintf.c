#include <stdio.h>

// This function returns the number of characters printed.
const int NAME = 8;
char filename[NAME];
int main(void)
{
    char buffer[13];

    int i = 50;
    sprintf(buffer, "This is CS%i\n", i);

    float f = 50.0;
    sprintf(buffer, "This is CS%.0f\n", f);
    printf("%s\n", buffer);

    sprintf(filename, "%03i.jpeg\n", 0);
}