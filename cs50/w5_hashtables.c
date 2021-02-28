
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// #include <cs50.h>

#define HASH_MAX 10

typedef struct node
{
    char* str;
    struct node *next;
}
node;

struct node *hashtable[HASH_MAX];

unsigned int generate_hash(char* str);
void insert(node **list, char* str);
node *create(char* str);
void print_hashtable(void);
void hash(char* str);
void print_list(node *list);
bool find(char* str);
int find_position(char* str);
void deleteMiddleNode(node *head, int position);
void deleteLastNode(node *head);
void deleteFirstNode(node **head);
void delete(char* str);

int main (void)
{
    char* s = "bude";
    hash(s);
    if (find(s))
    {
        printf("found\n");
    }
    // print_hashtable();
    delete(s);
    print_hashtable();
}

unsigned int generate_hash(char* str)
{
    int sum = 0;

    for (int j = 0; str[j] != '\0'; j++)
    {
        sum += str[j];
    }

    return sum % HASH_MAX;
}

void hash(char* str)
{
    unsigned int h = generate_hash(str);
    
    if (hashtable[h] == NULL)
    {
        node *list = create(str);
        hashtable[h] = list;
    }
    else
    {
        insert(&hashtable[h], str);
    }
}

node *create(char* str)
{
    node *list = malloc(sizeof(node));
    if (list == NULL)
    {
        return NULL;
    }
    list->str = str;
    list->next = NULL;

    return list;
}

void insert(node **list, char* str)
{
    node *n = malloc(sizeof(node));
    n->str = str;
    n->next = *list;

    *list = n;
}



void print_list(node *list)
{
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%s\n", tmp->str);
    }
}

void print_hashtable(void)
{
    for (int i = 0; i < HASH_MAX; i++)
    {
        print_list(hashtable[i]);
    }
}

bool find(char* str)
{
    unsigned int h = generate_hash(str);

    for (node *tmp = hashtable[h]; tmp != NULL; tmp = tmp->next)
    {
        if (tmp->str == str)
        {
            return true;
        }
    }

    return false;
}

int find_position(char* str)
{
    unsigned int h = generate_hash(str);
    int position = 0;

    for (node *tmp = hashtable[h]; tmp != NULL; tmp = tmp->next)
    {
        if (tmp->str == str)
        {
            break;
        }

        position++;
    }

    return position;
}

void deleteMiddleNode(node *head, int position)
{
    int i;
    struct node *toDelete, *prevNode;

    toDelete = head;
    prevNode = head;

    for (i = 2; i <= position; i++)
    {
        prevNode = toDelete;
        toDelete = toDelete->next;

        if (toDelete == NULL)
            break;
    }

    if (toDelete != NULL)
    {
        if (toDelete == head)
            head = head->next;

        prevNode->next = toDelete->next;
        toDelete->next = NULL;

        free(toDelete);
    }
    else
    {
        printf("Invalid position unable to delete.");
    }
}

void deleteLastNode(node *head)
{
    struct node *toDelete, *secondLastNode;

    if(head == NULL)
    {
        printf("List is already empty.");
    }
    else
    {
        toDelete = head;
        secondLastNode = head;

        while(toDelete->next != NULL)
        {
            secondLastNode = toDelete;
            toDelete = toDelete->next;
        }

        if(toDelete == head)
        {
            head = NULL;
        }
        else
        {
            secondLastNode->next = NULL;
        }

        free(toDelete);
    }
}

void deleteFirstNode(node **head)
{
    node *toDelete;

    if(*head == NULL)
    {
        printf("List is already empty.");
    }
    else
    {
        toDelete = *head;
        *head = (*head)->next;

        free(toDelete);
    }
}

void delete(char* str)
{
    int position = find_position(str);
    unsigned int h = generate_hash(str);

    if (position == 0)
    {
        deleteFirstNode(&hashtable[h]);
    }
    else if (hashtable[h]->next == NULL)
    {
        deleteLastNode(hashtable[h]);
    }
    else
    {
        deleteMiddleNode(hashtable[h], position);
    }
}