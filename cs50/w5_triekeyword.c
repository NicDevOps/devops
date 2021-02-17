#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

#define ALPHABET 26
const int CASE = 'a';

int MAXSIZE = 8;       
char stack[8 + 1];     
int top = -1;   

typedef struct node
{
    struct node* parent;
    struct node* children[ALPHABET];
    int occurence;
}node;

int isempty() 
{
   if(top == -1)
      return 1;
   else
      return 0;
}
   
int isfull() 
{
   if(top == MAXSIZE)
      return 1;
   else
      return 0;
}

char peek() 
{
   return stack[top];
}

char pop() 
{
   char data;
	
   if(!isempty()) 
   {
      data = stack[top];
      stack[top] = '\0';
      top = top - 1;  
      return data;
   } 
   else 
   {
      printf("Could not retrieve data, Stack is empty.\n");
   }
}

void push(char data) 
{
   if(!isfull()) 
   {
      top = top + 1;   
      stack[top] = data;
      stack[top + 1] = '\0';
   } 
   else 
   {
      printf("Could not insert data, Stack is full.\n");
   }
}

void insertNode(node* trieTree, char* word)
{
    node* currentNode = trieTree;

    while(*word != '\0')
    {
        int offset = *word - CASE;
        if (currentNode->children[offset] == NULL)
        {
            currentNode->children[offset] = malloc(sizeof(node));
            currentNode->children[offset]->parent = currentNode;
        }

        currentNode = currentNode->children[offset];
        ++word;
    }

    currentNode->occurence++;
}

node* searchNode(node* trieTree, char* word)
{
    while (*word != '\0')
    {  
        int offset = *word - CASE;
        if (trieTree->children[offset] != NULL)
        {
            trieTree = trieTree->children[offset];

            ++word;
        }
        else
        {
            return NULL;
        }
    }

    return (trieTree->occurence != 0) ? trieTree : NULL;
}

void deleteNode (node* trieTree, char* word)
{
    node* currentNode = searchNode(trieTree, word);

    if (currentNode != NULL)
    {
        --currentNode->occurence;
        node* parent = NULL;
        bool isLeaf = true;

        for (int i = 0; i < ALPHABET; ++i)
        {
            if (parent->children[i] == NULL)
            {

                isLeaf = false;
                break;
            }
        }

        while (currentNode->parent != NULL && isLeaf && currentNode->occurence == 0)
        {
            parent = currentNode->parent;
                
            for (int i = 0; i < ALPHABET; ++i)
            {
                if (parent->children[i] == currentNode)
                {
                    parent->children[i] = NULL;
                        
                    free(currentNode);
                    // delete currentNode;
                    currentNode = parent;/* code */
                }
                else if (parent->children[i] != NULL)
                {
                    isLeaf = false;
                    break;
                }
            }
        }  
    }
}

void PreOrderPrint(node* trieTree)
{
    if (trieTree->occurence > 0)
    {
        printf("%s %i\n", stack, trieTree->occurence);
        // for (auto it = word.begin(); it != word.end(); ++it)
        // {
        //     cout << *it;
        // }
        // cout << " " << trieTree->occurence << endl;
    }

    for (int i = 0; i < ALPHABET; ++i)
    {
        if (trieTree->children[i] != NULL)
        {
        // word.push_back(CASE + i);
            push(CASE + i);
            PreOrderPrint(trieTree->children[i]);
            pop();
        // word.pop_back();
        }
    }
}


int main ()
{
    node* root = malloc(sizeof(node));

    insertNode(root, "dude");
    insertNode(root, "mimi");
    insertNode(root, "winston");
    insertNode(root, "legros");
    insertNode(root, "mimi");
    // deleteNode(root, "mimi");
    PreOrderPrint(root);
}