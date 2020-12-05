#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>

int encrypt(string plain, string cipher, string sub);

int main(int argc, string argv[])
{
    string p = get_string("plaintext: ");
    string c = "abcdefghijklmnopqrstuvwxyz";
    string s = argv[1];

    if (argc == 2)
    {
        if (strlen(s) == 26)
        {
            for (int i = 0, n = strlen(s); i < n; i++)
            {
                if (ispunct(s[i]))
                {
                    printf("invalid key");
                    return 1;
                }
                else if (isdigit(s[i]))
                {
                    printf("invalid key");
                    return 1; 
                }
                else if (isspace(s[i]))
                {
                    printf("invalid key");
                    return 1;
                }
                else
                {
                    int r = 0;
                    for (int j = 0, n = strlen(s); j < n; j++)
                    {   
                        if (tolower(s[i]) == tolower(s[j]))
                        {
                            r++;
                        }
                    }
                    if (r > 1)
                    {
                        printf("Invalid key, dont do doubles!");
                        return 1;
                    }
                }
            }
            printf("ciphertext: ");
            encrypt(p, c, s);
            return 0;  
        }
    }
}
int encrypt(string plain, string cipher, string sub)
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
                printf("%c", tolower(sub[i]));
            }
            else if (isupper(plain[j]))
            {
                int h = tolower(plain[j]);
                if (cipher[i] == h)
                {
                    printf("%c", toupper(sub[i]));
                }
            }        
        } 
    }
    printf("\n");
}