#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCKSIZE 512
#define NAME 10

// const int BLOCKSIZE = 512;
// const int NAME = 8;

typedef uint8_t BYTE;
typedef struct
{
    BYTE buffer[BLOCKSIZE];
}
BLOCK;

char filename[NAME];

int main(int argc, char *argv[])
{
     // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Open memory files
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    sprintf(filename, "%03i.jpg\n", 0);
    FILE *img = fopen(filename, "w");
    if (img == NULL)
    {
        fclose(input);
        return 1;
    }

    BLOCK c;
    int n = 0;
    
    while (fread(&c, sizeof(BLOCKSIZE), 1, input))
    {
        if (c.buffer[0] == 0xff && c.buffer[1] == 0xd8 && c.buffer[2] == 0xff && (c.buffer[3] & 0xf0) == 0xe0)
        {
            if (n == 0)
            {
                fwrite(&c, sizeof(BLOCKSIZE), 1, img);
                n++;
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg\n", n);
                FILE *img = fopen(filename, "w");
                fwrite(&c, sizeof(BLOCKSIZE), 1, img);
                n++;
            }
        }
        else
        {
            if (n != 0)
            {
                fwrite(&c, sizeof(BLOCKSIZE), 1, img);
            }
            else
            {
                continue;
            }
        }
    }

    fclose(input);
}