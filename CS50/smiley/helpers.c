#include "helpers.h"
#include <stdio.h>

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through picture

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Colorize pixel to green
            if (image[i][j].rgbtRed == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtBlue == 0x00)
            {
                image[i][j].rgbtGreen = 0xff;

            }
        }
    }
}