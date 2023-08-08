#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startpop;
    do
    {
        startpop = get_int("Start size: ");
    }
    while (startpop < 9);
    // TODO: Prompt for end size
    int endpop;
    do
    {
        endpop = get_int("End size: ");
    }
    while (endpop < startpop);
    // TODO: Calculate number of years until we reach threshold
    int counter = 0;
    while (startpop < endpop)
    {
        startpop = startpop + (startpop / 3) - (startpop / 4);
        counter++;
    }
    // TODO: Print number of years
    printf("Years: %i\n", counter);
}
