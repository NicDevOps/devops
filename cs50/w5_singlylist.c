// Implements a list of numbers with linked list

#include <stdio.h>
#include <stdlib.h>

// Represents a node
typedef struct node
{
    int number;
    struct node *next;
}
node;

node *create(int val);
node *insert(node *list, int val);
node *sort(node *list);
void print_list(node *list);
void free_list(node *list);

int main(void)
{
    node *numbers = create(1);
    numbers = insert(numbers, 2);
    numbers = insert(numbers, 3);
    print_list(numbers);
    free_list(numbers);
    return 0;
}

node *create(int val)
{
    node *list = NULL;
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return NULL;
    }
    n->number = val;
    n->next = NULL;
    list = n;

    return list;
}

void print_list(node *list)
{
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
}

void free_list(node *list)
{
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
}

node *insert(node *list, int val)
{
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return NULL;
    }
    n->number = val;
    n->next = list;

    list = n;

    return list;
}

node *sort(node *list)
{
    for (node *head = list; head != NULL; head = head->next)
    {
        for (node *tmp = head; tmp != NULL; tmp = tmp->next)
        {
            if (tmp->number > tmp->next->number)
            {
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
            }
        }
    }
}