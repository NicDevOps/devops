#include <stdio.h>
#include <string.h>
#include <math.h>
#include "cs50.h"

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  \n");

    // string s = "Congratulations! Today is your day. You're off to Great Places! You're off and away!";

    int letter = 0;
    int word = 0;
    int sentence = 0;
    int j = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'A' && s[i] <= 'z')
        {
            ++letter;
            ++j;
        } 
        else if (s[i] == ' ')
        {
            if (j > 0)
            {
                ++word;
                j = 0;
            }
        }
        else if (s[i] >= 34 && s[i] <= 45 || s[i] == 47 || s[i] >= 58 && s[i] <= 62 || s[i] == 64 || s[i] >= 91 && s[i] <= 96 || s[i] >= 123 && s[i] <= 255)
        {
            continue;
        }      
        else if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            if (j == 0)
            {
                --sentence;
            }
            ++sentence;
            if (j > 0)
            {
                ++word;
                j = 0;
            }        
        }
    }
    float L = (letter * 100) / word;
    float S = (sentence * 100) / word;
    float grade = round(0.0588 * L - 0.296 * S - 15.8);

    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", grade);
    }
    printf("\n");
}