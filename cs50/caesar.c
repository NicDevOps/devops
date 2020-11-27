#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>

int encrypt(string plain, string cipher, int key);

int main(int argc, char *argv[])
{
    string p = get_string("Enter a secret: ");
    string c = "abcdefghijklmnopqrstuvwxyz";
    if (argc == 2)
    {
        int k = atoi(argv[1]);
    
        if (isdigit(k))
        {
            printf("Must be a positive integer");
        }
        else
        {
            encrypt(p, c, k);
        }
    }
    else
    {
        printf("Missing Key argument");
    }
}

int encrypt(string plain, string cipher, int key)
{
    for (int j = 0, m = strlen(plain); j < m; j++)
    {
        if (ispunct(plain[j]))
        {
            printf("%c", plain[j]);
        }
        else if (isspace(plain[j]))
        {
            printf("%c", plain[j]); 
        }
        else if (isdigit(plain[j]))
        {
            printf("%c", plain[j]);
        } 
        for (int i = 0, n = strlen(cipher); i < n; i++)
        {
            if (cipher[i] == plain[j])
            {
                printf("%c", cipher[(i + key) % 26]);
            }
            else if (isupper(plain[j]))
            {
                int h = tolower(plain[j]);
                if (cipher[i] == h)
                {
                    printf("%c", toupper(cipher[(i + key) % 26]));
                }
            }        
        } 
    }
    printf("\n");
}