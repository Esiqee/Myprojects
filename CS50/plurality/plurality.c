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
bool vote(string name)
{
    //loop through candidates
    for (int j = 0; j < candidate_count; j++)
    {
        //if candidate matches vote input add+1 to votes
        if (strcmp(candidates[j].name, name) == 0)
        {
            candidates[j].votes += 1;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    //Create max vote & loop through votes to find who has most of em
    int maxvotes = candidates[0].votes;
    for (int k = 0; k < candidate_count; k++)
    {
        if (maxvotes < candidates[k].votes)
        {
            maxvotes = candidates[k].votes;
        }
    }
    // loop once again and print those names who has highest amount of votes
    for (int l = 0; l < candidate_count; l++)
    {
        if (maxvotes == candidates[l].votes)
        {
            printf("%s\n", candidates[l].name);
        }
    }
    return;
}