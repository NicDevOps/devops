#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
bool check_cycle();
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
int mag(pair p);


int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    // int voter_count = get_int("Number of voters: ");

    // Query for votes
    // for (int i = 0; i < voter_count; i++)
    // {
    //     // ranks[i] is voter's ith preference
    //     int ranks[candidate_count];

    //     // Query for each rank
    //     for (int j = 0; j < candidate_count; j++)
    //     {
    //         string name = get_string("Rank %i: ", j + 1);

    //         if (!vote(j, name, ranks))
    //         {
    //             printf("Invalid vote.\n");
    //             return 3;
    //         }
    //     }

    //     record_preferences(ranks);

    //     printf("\n");
    // }

    int ranks[candidate_count];

    vote(0, "alice", ranks);
    vote(1, "bob", ranks);
    vote(2, "charlie", ranks);
    record_preferences(ranks);

    vote(0, "alice", ranks);
    vote(1, "bob", ranks);
    vote(2, "charlie", ranks);
    record_preferences(ranks);

    vote(0, "alice", ranks);
    vote(1, "bob", ranks);
    vote(2, "charlie", ranks);
    record_preferences(ranks);

    vote(0, "bob", ranks);
    vote(1, "charlie", ranks);
    vote(2, "alice", ranks);
    record_preferences(ranks);

    vote(0, "bob", ranks);
    vote(1, "charlie", ranks);
    vote(2, "alice", ranks);
    record_preferences(ranks);

    vote(0, "charlie", ranks);
    vote(1, "alice", ranks);
    vote(2, "bob", ranks);
    record_preferences(ranks);

    vote(0, "charlie", ranks);
    vote(1, "alice", ranks);
    vote(2, "bob", ranks);
    record_preferences(ranks);

    vote(0, "charlie", ranks);
    vote(1, "alice", ranks);
    vote(2, "bob", ranks);
    record_preferences(ranks);

    vote(0, "charlie", ranks);
    vote(1, "alice", ranks);
    vote(2, "bob", ranks);
    record_preferences(ranks);

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[i] = rank;
            return true;
        }
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (i != j)
            {
                if (ranks[i] < ranks[j])
                {
                    preferences[i][j]++;
                }
            }
        }
    }
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = candidate_count * (candidate_count - 1) / 2;

    for (int i = 0; i < pair_count; i++)
    {
        for (int j = 0; j < pair_count; j++)
        {
            printf("%s over %s\n", candidates[i], candidates[j]);

            if (i != j)
            {
                if (preferences[i][j] > preferences[j][i])
                {
                    pairs[i].winner = preferences[i][j];
                    pairs[i].loser = preferences[j][i];
                    break;
                }
            }
        }
    }

    for (int i = 0; i < pair_count; i++)
    {
        printf("winner: %i\n", pairs[i].winner);
        printf("loser: %i\n", pairs[i].loser);
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for (int step = 0; step < pair_count - 1; ++step) 
    {
        for (int i = 0; i < pair_count - step - 1; ++i) 
        {
            int h = mag(pairs[i]);
            int k = mag(pairs[i + 1]);
            
            if (h < k) 
            {  
                pair temp = pairs[i];
                pairs[i] = pairs[i + 1];
                pairs[i + 1] = temp;
            }
        }
    }

    printf("\n");
    for (int i = 0; i < pair_count; i++)
    {
        printf("winner: %i\n", pairs[i].winner);
        printf("loser: %i\n", pairs[i].loser);
    }
}

int mag(pair p)
{
    return p.winner - p.loser;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{   
    for (int p = 0; p < pair_count; p++)
    {
        for (int i = 0; i < candidate_count; i++)
        {
            for (int j = 0; j < candidate_count; j++)
            {
                if (i != j)
                {
                    if (preferences[i][j] == pairs[p].winner && preferences[j][i] == pairs[p].loser)
                    {
                        locked[i][j] = true;
                        if (check_cycle() == true)
                        {
                            locked[i][j] = false;
                            continue;
                        }
                        printf("Pair (%s over %s) is locked\n", candidates[i], candidates[j]);
                    }
                }
            }
        }  
    }
}

bool check_cycle()
{
    int h = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (i != j)
            {
                if (locked[i][j] == true)
                {
                    h++;
                }
            }
        }
    }

    if (h == candidate_count)
    {
        return true;
    }
    else
    {
        return false; 
    }
}

// Print the winner of the election
void print_winner(void)
{
    int loser[candidate_count];

    for (int i = 0; i < candidate_count; i++)
    {
        loser[i] = 0;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (i != j)
            {
                if (locked[i][j] == true)
                {
                    printf("%s over %s\n", candidates[i], candidates[j]);
                    loser[j]++;
                }
            }
        }
    }
    
    for (int i = 0; i < candidate_count; i++)
    {
        if (loser[i] == 0)
        {
            printf("The winner of this election is: %s\n", candidates[i]);
        }
    }
}