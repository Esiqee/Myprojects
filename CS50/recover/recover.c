#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //Arg check
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //open memory card
    FILE *file = fopen(argv[1], "r");
    //check if we can open file
    if (file == NULL)
    {
        printf("Couldn't open file\n");
        return 1;
    }

    //create buffer
    typedef uint8_t  BYTE;
    BYTE buffer[512];
    // count how many pictures we got
    int pics = 0;
    int i = 0;

    //Repeat until end of card & read 512 bytes into buffer
    while (fread(buffer, 512, 1, file) == 1)
    {
        //if we find header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0 && file != NULL)
        {
            //control if its first jpg
            if (i == 0)
            {
                i ++;
            }
            // if its not first jpg add pics counter so we can create new file
            else if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0 && file != NULL && i != 0)
            {
                pics ++;
            }
        }
        //open img to write in
        char filename[8];
        sprintf(filename, "%03i.jpg", pics);
        FILE *img = fopen(filename, "a");

        //if chunk has data inside write it to file
        if (file != NULL && i != 0)
        {
            fwrite(buffer, 512, 1, img);
        }
        fclose(img);
    }
    fclose(file);
}
