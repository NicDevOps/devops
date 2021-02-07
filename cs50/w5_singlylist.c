// Implements a list of numbers with linked list
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

// Represents a node
typedef struct node
{
    int number;
    struct node *next;
}
node;

node *create(int val);
void insert(node **list, int val);
void delete(node *list, int val);
void deleteMiddleNode(node *head, int position);
void deleteFirstNode(node **head);
void deleteLastNode(node *head);
void sort(node *list);
void print_list(node *list);
void free_list(node *list);
bool find(node *list, int val);

int main(void)
{
    node *numbers = create(1);
    insert(&numbers, 2);
    insert(&numbers, 3);
    insert(&numbers, 4);
    insert(&numbers, 5);
    sort(numbers);
    if (find(numbers, 2))
    {
        printf("found\n");
    }
    deleteFirstNode(&numbers);
    // deleteMiddleNode(numbers, 3);
    // delete(numbers, 2);
    // deleteLastNode(numbers);
    print_list(numbers);
    free_list(numbers);
    return 0;
}

node *create(int val)
{
    node *list = malloc(sizeof(node));
    if (list == NULL)
    {
        return NULL;
    }
    list->number = val;
    list->next = NULL;

    return list;
}

void print_list(node *list)
{
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
}

bool find(node *list, int val)
{
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        if (tmp->number == val)
        {
            return true;
        }
    }

    return false;
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

void insert(node **list, int val)
{
    node *n = malloc(sizeof(node));
    n->number = val;
    n->next = *list;

    *list = n;
}

void sort(node *list)
{
    for (node *head = list; head != NULL; head = head->next)
    {
        for (node *tmp = list; tmp->next != NULL; tmp = tmp->next)
        {
            if (tmp->number > tmp->next->number)
            { 
                int temp = tmp->number;
                tmp->number = tmp->next->number;
                tmp->next->number = temp;
            }
        }
    }
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

        /* Delete nth node */
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

        /* Traverse to the last node of the list */
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
            /* Disconnect link of second last node with last node */
            secondLastNode->next = NULL;
        }

        /* Delete the last node */
        free(toDelete);

        printf("SUCCESSFULLY DELETED LAST NODE OF LIST\n");
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

        printf("\nData deleted = %d\n", toDelete->number);

        /* Clears the memory occupied by first node*/
        free(toDelete);

        printf("SUCCESSFULLY DELETED FIRST NODE FROM LIST\n");
    }
}
