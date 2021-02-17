#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

#define TRIE_MAX 4

typedef struct _trie
{
    char* university[20];
    struct _trie* paths[10];
}
_trie;

_trie *node;
// _trie *create(char* str);

void trie(char* str, char* year);
void print_trie(char* year);

int main(void)
{
    char* university = {"harvard"};
    char* year = {"2021"};
    trie(university, year);
    print_trie(year);
}

void trie(char* str, char* year)
{
    for (int i = 0; i < TRIE_MAX; i++)
    {
        int x = atoi(year[i]);

        if (node->paths[i] == NULL)
        {
            create_node(x);
        }
        else if (i == TRIE_MAX)
        {
            create_leaf(str, x);
        }
        else
        {
            insert_node(x);
        }
    }
}

void print_trie(char* year)
{
    for (int i = 0; i < sizeof(year) / 2; i++)
    {
        printf("%c\n", year[i]);
    }
}


// void insertNodeAtEnd(int data)
// {
//     struct node *newNode, *temp;

//     newNode = (struct node*)malloc(sizeof(struct node));

//     if(newNode == NULL)
//     {
//         printf("Unable to allocate memory.");
//     }
//     else
//     {
//         newNode->data = data; // Link the data part
//         newNode->next = NULL; 

//         temp = head;

//         // Traverse to the last node
//         while(temp != NULL && temp->next != NULL)
//             temp = temp->next;

//         temp->next = newNode; // Link address part

//         printf("DATA INSERTED SUCCESSFULLY\n");
//     }
// }