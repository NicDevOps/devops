// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "zdictionary.h"

#define N 1000
// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
// const unsigned int N = 1;

// Hash table
node *table[N];

unsigned int loaded = 0;

void hashtable(char* word);
node *create(char* word);
void insert(node **list, char* str);
void print_hashtable(void);
void print_list(node *list);
void free_list(node *list);

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int h = hash(word);

    for (node *tmp = table[h]; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;

    for (int j = 0; word[j] != '\0'; j++)
    {
        sum += word[j];
    }

    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file != NULL)
    {
        char word[LENGTH + 1];
        // printf("%s\n", c);
        while (fscanf(file, "%s", word) != EOF)
        {
            // printf("%s\n", word);
            hashtable(word);
            loaded++;
        }
        fclose(file);
        print_hashtable();

        return true;
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return loaded;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        free_list(table[i]);
    }
    return loaded == 0;
}

void hashtable(char* word)
{
    unsigned int h = hash(word);
    
    if (table[h] == NULL)
    {
        node *list = create(word);
        table[h] = list;
    }
    else
    {
        insert(&table[h], word);
    }
}

node *create(char* word)
{
    node *list = malloc(sizeof(node));
    if (list == NULL)
    {
        return NULL;
    }
    strcpy(list->word, word);
    list->next = NULL;

    return list;
}

void insert(node **list, char* str)
{
    node *n = malloc(sizeof(node));
    strcpy(n->word, str);
    n->next = *list;

    *list = n;
}

void print_list(node *list)
{
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%s\n", tmp->word);
    }
}

void print_hashtable(void)
{
    for (int i = 0; i < N; i++)
    {
        print_list(table[i]);
    }
}

void free_list(node *list)
{
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;

        loaded--;
    }
}