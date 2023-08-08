#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //Convert argv in string

   string arginput = argv[1];

    // getting sure input is a number and has only one argument
    // if not reprompt user with printf("Usage: ./caesar key\n");

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    for (int l = 0, len = strlen(arginput); l < len; l++)
        if (!isdigit(arginput[l]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }

    // test cases passed
    // get plaintext & convert arg to int

int inp = atoi(arginput);
string plaintext = get_string("Plaintext: ");

// Print Ciphertext and add converted letters

printf("Ciphertext: ");

    // convert letters to ciphertext
    for (int i = 0, lenn = strlen(plaintext); i < lenn; i++)
        if (isupper(plaintext[i]))
        {
            printf("%c", (plaintext[i] - 65 + inp)%26 +65);
        }
        else if (islower(plaintext[i]))
        {
            printf("%c", (plaintext[i] - 97 + inp)%26 +97);
        }
        else if (!isalpha(plaintext[i]))
        {
            printf("%c", plaintext[i]);
        }
printf("\n");
}
