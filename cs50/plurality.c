#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string s)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, s) == 0)
        {
            printf("Found\n");
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int size = candidate_count;
    for (int step = 0; step < size - 1; ++step) 
    {
        for (int i = 0; i < size - step - 1; ++i) 
        {
        // To sort in descending order, change">" to "<".
            if (candidates[i].votes < candidates[i + 1].votes) 
            {  
            // swap if greater is at the front position
            string temp_1 = candidates[i].name;
            int temp_2 = candidates[i].votes;

            candidates[i].name = candidates[i + 1].name;
            candidates[i].votes = candidates[i + 1].votes;

            candidates[i + 1].name = temp_1;
            candidates[i + 1].votes = temp_2;
            }
        }
    }
    for (int i = 0; i < size; ++i) 
    {
        printf("%s  ", candidates[i].name);
    }
    printf("\n");
    for (int i = 0; i < size; ++i) 
    {
        printf("%i  ", candidates[i].votes);
    }
    printf("\n");
    if (candidates[0].votes > candidates[1].votes)
    {
        printf("%s is the winner!(%i)\n", candidates[0].name, candidates[0].votes);
    }
    else
    {
        for (int i = 0; i < size; ++i)
        { 
            if (candidates[i].votes == candidates[i + 1].votes)
            {
                printf("%s is a winner!(%i)\n", candidates[i].name, candidates[i].votes);
            }
            else if (candidates[i].votes == candidates[i - 1].votes)
            {
                printf("%s is a winner!(%i)\n", candidates[i].name, candidates[i].votes);
                i = size;
            }
        }
    } 
}


