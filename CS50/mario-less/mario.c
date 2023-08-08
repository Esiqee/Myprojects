#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    // print pyramid
    //newline function
    for (int line = 0; line < height; line++)
    {
        //dots
        for (int dots = height - 1; dots > line; dots--)
        {
            printf(" ");
        }
        //hash
        for (int hash = -1; hash < line; hash++)
        {
            printf("#");
        }
        printf("\n");
    }

}