#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCKSIZE 512
#define NAME 8

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

    // FILE *img = NULL;
    sprintf(filename, "%03i.jpg", 0);
    FILE *img = fopen(filename, "w");
    BLOCK c;
    int n = 0;

    // printf("%li\n", sizeof(BLOCK));
    // printf("%s\n", c.buffer);
    // int bytes_read = fread(&c, sizeof(BLOCKSIZE), 1, input);

    // printf("%i\n", bytes_read);
    // printf("%s\n", c.buffer);
    // bool header_found = false;

    // while (bytes_read)
    // {
    //     if (c.buffer[0] == 0xff && c.buffer[1] == 0xd8 && c.buffer[2] == 0xff && (c.buffer[3] & 0xf0) == 0xe0)
    //     {
    //         if (header_found == false)
    //         {
    //             sprintf(filename, "%03i.jpg", n);
    //             img = fopen(filename, "w");
    //             printf("first_header %i\n", n);
    //             fwrite(&c, sizeof(BLOCKSIZE), 1, img);
    //             header_found = true;
    //         }
    //         else
    //         {
    //             fclose(img);
    //             n++;
    //             sprintf(filename, "%03i.jpg", n);
    //             img = fopen(filename, "w");
    //             printf("header %i\n", n);
    //             fwrite(&c, sizeof(BLOCKSIZE), 1, img); 
    //         }
    //     }
    //     else
    //     {
    //         // printf("chunk %i\n", n);
    //         if (header_found == true)
    //         {
    //             fwrite(&c, sizeof(BLOCKSIZE), 1, img);
    //         }
           
    //     }
    //     // printf("%i\n", bytes_read);
    //     bytes_read = fread(&c, sizeof(BLOCKSIZE), 1, input);
    // }
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
                sprintf(filename, "%03i.jpg", n);
                img = fopen(filename, "w");
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
    
    fclose(img);
    fclose(input);
}