#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 45

int main(void)
{
    char *s = get_string("s: ");
    if (s != NULL)
    {
        char word[LENGTH + 1];
        // char *t = malloc(strlen(s) + 1);
        if (word != NULL)
        {
            strcpy(word, s);
            printf("s: %s\n", s);
            printf("t: %s\n", word);
        }
    }
}