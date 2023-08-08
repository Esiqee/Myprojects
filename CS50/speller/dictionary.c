// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

int dictsize = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash word to obtain hash value
    int hashval = hash(word);

    // Access linked list at that index in the hash table
    node *cursor = table[hashval];

    // Traverse linked list, looking for word (strcasecmp)
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int wchar0 = 0;
    int wchar1 = 0;

    wchar0 = toupper(word[0]) - 'A';
    //handles 1 char words, segfault fix
    if (toupper(word[1]) == '\0')
    {
        wchar1 = 0;
    }
    else
    {
        wchar1 = toupper(word[1]) - 'A';
    }

    int hashed_number = 0;

    // Handles words starting with A (AA-AZ) hashes 0-25 so we wont multiply by 0
    if (wchar0 == 0)
    {
        hashed_number = wchar1;
    }
    // Handles words starting with BA-ZZ hashes 26-675 while ZZ is 675
    // eg. BA = 1*26+0 = 26 , ZZ = 25*26+25 = 675
    else if (wchar0 != 0)
    {
        hashed_number = wchar0 * 26 + wchar1;
    }

    return hashed_number;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    // TODO
    // Open file
    FILE *dict = fopen(dictionary, "r");

    // Check if file exists
    if (dictionary == 0)
    {
        printf("Couldn't open dictionary");
        return false;
    }

    // Make word array
    char wordfromdict[LENGTH + 1];

    // Read words from file
    while (fscanf(dict, "%s", wordfromdict) != EOF)
    {

        // Create a new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Problem with dictionary memory allocation");
            return false;
        }

        // Copy word into node
        strcpy(n->word, wordfromdict);

        // Hash word using hash function
        int index = hash(wordfromdict);

        // Prepend node into hash table list
        n->next = table[index];
        table[index] = n;
        dictsize ++;

    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // word counter is implemented while dictionary words are loading
    return dictsize;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Loop through hash table
    for (int i = 0; i < N; i++)
    {
        // Assign cursor into row by row in hash table
        node *cursor = table[i];
        // Loop through the list untill we hit end of list (NULL)
        while (cursor != NULL)
        {
            // Create tmp cursor pointing to the same node
            node *tmp = cursor;
            // Point cursor to next before we free first element
            cursor = cursor->next;
            // Free first element
            free(tmp);
        }
        if (cursor == NULL)
        {
            free(cursor);
        }
    }
    return true;
}
