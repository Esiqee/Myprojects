#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    //first lets get input
    string sentence = get_string("Text: ");

    //Count letters
    int letters = 0;
    for (int l = 0, len = strlen(sentence); l < len; l++)
    {
        if (isupper(sentence[l]))
        {
            letters ++;
        }
        else if (islower(sentence[l]))
        {
            letters ++;
        }
    }

    // Count words
    int words = 1;
    for (int l = 0, len = strlen(sentence); l < len; l++)
    {
        if (sentence[l] == ' ')
        {
            words ++;
        }
    }

    // Count sentences
    int sent = 0;
    for (int l = 0, len = strlen(sentence); l < len; l++)
    {
        if (sentence[l] == '.')
        {
            sent ++;
        }
        else if (sentence[l] == '?')
        {
            sent ++;
        }
        else if (sentence[l] == '!')
        {
            sent ++;
        }
    }
    // counting idnex
    float L = 0;
    float S = 0;
    float index = 0;
    float let = (float) letters;
    float sen = (float) sent;
    float wor = (float) words;
    L = let / wor * 100.0;
    S = sen / wor * 100.0;
    index = 0.0588 * L - 0.296 * S - 15.8;


    // to the nerest whole number
    if (index < 0.99)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 0.99 && index < 2.449)
    {
        printf("Grade 2\n");
    }
    else if (index > 2.45 && index < 3.4449)
    {
        printf("Grade 3\n");
    }
    else if (index > 3.45 && index < 4.449)
    {
        printf("Grade 4\n");
    }
    else if (index > 4.45 && index < 5.449)
    {
        printf("Grade 5\n");
    }
    else if (index > 5.45 && index < 6.449)
    {
        printf("Grade 6\n");
    }
    else if (index > 6.45 && index < 7.49)
    {
        printf("Grade 7\n");
    }
    else if (index > 7.5 && index < 8.449)
    {
        printf("Grade 8\n");
    }
    else if (index > 8.45 && index < 9.449)
    {
        printf("Grade 9\n");
    }
    else if (index > 9.45 && index < 10.449)
    {
        printf("Grade 10\n");
    }
    else if (index > 10.45 && index < 11.449)
    {
        printf("Grade 11\n");
    }
    else if (index > 11.45 && index < 12.449)
    {
        printf("Grade 12\n");
    }
    else if (index > 12.45 && index < 13.449)
    {
        printf("Grade 13\n");
    }
    else if (index > 13.45 && index < 14.449)
    {
        printf("Grade 14\n");
    }
    else if (index > 14.45 && index < 15.449)
    {
        printf("Grade 15\n");
    }
    else
    {
        printf("Grade 16+\n");
    }

//printf ("%i letters\n", letters);
//printf ("%i words\n", words);
//printf ("%i sentences\n", sent);
//printf ("%f Index\n", index);

    //printf("%s\n", sentence);
}