#include <stdio.h>
#include <stdlib.h>


typedef struct
{
    int age;
    int hp;
}
PERSONTYPE;

int main (void)
{
    PERSONTYPE *black = malloc(sizeof(PERSONTYPE));

    black->age = 55;
    black->hp = 10;
    // *(black).age = 55;
    // *(black).hp = 10;
    printf("%i is %i\n", black->hp, black->age);
    free(black);
    // int *a = malloc(sizeof(int));
    // // int *a = NULL;
    // // a = malloc(sizeof(int));
    // *a = 255;
    // printf("%i\n", *a);
    // free(a);

    // char word[] = "cat";
    // printf("%s\n", word);

    // for (char *letter = word; *letter != '\0'; letter++)
    // {
    //     printf("%s\n", letter);
    //     printf("%c\n", *letter);
    // }


}