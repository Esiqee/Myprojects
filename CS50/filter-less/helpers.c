#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through all the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //get grey amount, find average velue, round it and assign to the pixel
            float grey = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            int greyrounded = round(grey);
            image[i][j].rgbtGreen = greyrounded;
            image[i][j].rgbtRed = greyrounded;
            image[i][j].rgbtBlue = greyrounded;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //loop through all the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //apply sepia algorythm
            float sepiared = (image[i][j].rgbtRed * 0.393 + image[i][j].rgbtGreen * 0.769 + image[i][j].rgbtBlue * 0.189);
            float sepiablue = (image[i][j].rgbtRed * 0.272 + image[i][j].rgbtGreen * 0.534 + image[i][j].rgbtBlue * 0.131);
            float sepiagreen = (image[i][j].rgbtRed * 0.349 + image[i][j].rgbtGreen * 0.686 + image[i][j].rgbtBlue * 0.168);
            int sepiaredround = round(sepiared);
            if (sepiaredround > 255)
            {
                sepiaredround = 255;
            }
            int sepiablueround = round(sepiablue);
            if (sepiablueround > 255)
            {
                sepiablueround = 255;
            }
            int sepiagreenround = round(sepiagreen);
            if (sepiagreenround > 255)
            {
                sepiagreenround = 255;
            }
            image[i][j].rgbtGreen = sepiagreenround;
            image[i][j].rgbtRed = sepiaredround;
            image[i][j].rgbtBlue = sepiablueround;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //loop in rows
    for (int i = 0; i < height; i++)
    {
        // this if statement will work for cases when width length is even, otherwise we use else function for odd cases
        if (width % 2 == 0)
        {
            //find midpoint in the line
            int middle = width / 2;
            //loop in column and swap elements
            for (int j = 0; j < middle; j++)
            {
                RGBTRIPLE temp = image[i][j];
                image [i][j] = image[i][width - j - 1];
                image[i][width - j - 1] = temp;
            }

        }
        else
        {
            //find middle element in the line
            float midelementfl = width / 2.0 - 0.5;
            int midelement = midelementfl;
            //loop in column and swap elements
            for (int j = 0; j < midelement; j++)
            {
                RGBTRIPLE temp = image[i][j];
                image [i][j] = image[i][width - j - 1];
                image[i][width - j - 1] = temp;
            }

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Perservation of original image
    RGBTRIPLE original[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            original[i][j] = image[i][j];
        }
    }
    // Blur corners

    // corner 1
    float corner1ravg = (original[0][0].rgbtRed + original[0][1].rgbtRed + original[1][0].rgbtRed + original[1][1].rgbtRed) / 4.0;
    int corner1red = round(corner1ravg);
    float corner1gavg = (original[0][0].rgbtGreen + original[0][1].rgbtGreen + original[1][0].rgbtGreen + original[1][1].rgbtGreen) /
                        4.0;
    int corner1green = round(corner1gavg);
    float corner1bavg = (original[0][0].rgbtBlue + original[0][1].rgbtBlue + original[1][0].rgbtBlue + original[1][1].rgbtBlue) / 4.0;
    int corner1blue = round(corner1bavg);
    image[0][0].rgbtRed = corner1red;
    image[0][0].rgbtGreen = corner1green;
    image[0][0].rgbtBlue = corner1blue;

    //corner 2

    float corner2ravg = (original[0][width - 1].rgbtRed + original[0][width - 2].rgbtRed + original[1][width - 1].rgbtRed +
                         original[1][width - 2].rgbtRed) / 4.0;
    int corner2red = round(corner2ravg);
    float corner2gavg = (original[0][width - 1].rgbtGreen + original[0][width - 2].rgbtGreen + original[1][width - 1].rgbtGreen +
                         original[1][width - 2].rgbtGreen) / 4.0;
    int corner2green = round(corner2gavg);
    float corner2bavg = (original[0][width - 1].rgbtBlue + original[0][width - 2].rgbtBlue + original[1][width - 1].rgbtBlue +
                         original[1][width - 2].rgbtBlue) / 4.0;
    int corner2blue = round(corner2bavg);
    image[0][width - 1].rgbtRed = corner2red;
    image[0][width - 1].rgbtGreen = corner2green;
    image[0][width - 1].rgbtBlue = corner2blue;

    //corner 3

    float corner3ravg = (original[height - 1][0].rgbtRed + original[height - 1][1].rgbtRed + original[height - 2][0].rgbtRed +
                         original[height - 2][1].rgbtRed) / 4.0;
    int corner3red = round(corner3ravg);
    float corner3gavg = (original[height - 1][0].rgbtGreen + original[height - 1][1].rgbtGreen + original[height - 2][0].rgbtGreen +
                         original[height - 2][1].rgbtGreen) / 4.0;
    int corner3green = round(corner3gavg);
    float corner3bavg = (original[height - 1][0].rgbtBlue + original[height - 1][1].rgbtBlue + original[height - 2][0].rgbtBlue +
                         original[height - 2][1].rgbtBlue) / 4.0;
    int corner3blue = round(corner3bavg);
    image[height - 1][0].rgbtRed = corner3red;
    image[height - 1][0].rgbtGreen = corner3green;
    image[height - 1][0].rgbtBlue = corner3blue;

    //corner 4

    float corner4ravg = (original[height - 1][width - 1].rgbtRed + original[height - 1][width - 2].rgbtRed + original[height - 2][width
                         - 1].rgbtRed + original[height - 2][width - 2].rgbtRed) / 4.0;
    int corner4red = round(corner4ravg);
    float corner4gavg = (original[height - 1][width - 1].rgbtGreen + original[height - 1][width - 2].rgbtGreen + original[height -
                         2][width - 1].rgbtGreen + original[height - 2][width - 2].rgbtGreen) / 4.0;
    int corner4green = round(corner4gavg);
    float corner4bavg = (original[height - 1][width - 1].rgbtBlue + original[height - 1][width - 2].rgbtBlue + original[height -
                         2][width - 1].rgbtBlue + original[height - 2][width - 2].rgbtBlue) / 4.0;
    int corner4blue = round(corner4bavg);
    image[height - 1][width - 1].rgbtRed = corner4red;
    image[height - 1][width - 1].rgbtGreen = corner4green;
    image[height - 1][width - 1].rgbtBlue = corner4blue;

    //Edges

    //bottom

    for (int j = 1; j < width - 1; j++)
    {
        float bottomredavg = (original[0][j - 1].rgbtRed + original[1][j - 1].rgbtRed + original[0][j].rgbtRed + original[1][j].rgbtRed +
                              original[0][j + 1].rgbtRed + original[1][j + 1].rgbtRed) / 6.0;
        int bottomred = round(bottomredavg);
        float bottomgreenavg = (original[0][j - 1].rgbtGreen + original[1][j - 1].rgbtGreen + original[0][j].rgbtGreen +
                                original[1][j].rgbtGreen + original[0][j + 1].rgbtGreen + original[1][j + 1].rgbtGreen) / 6.0;
        int bottomgreen = round(bottomgreenavg);
        float bottomblueavg = (original[0][j - 1].rgbtBlue + original[1][j - 1].rgbtBlue + original[0][j].rgbtBlue + original[1][j].rgbtBlue
                               + original[0][j + 1].rgbtBlue + original[1][j + 1].rgbtBlue) / 6.0;
        int bottomblue = round(bottomblueavg);

        image[0][j].rgbtRed = bottomred;
        image[0][j].rgbtGreen = bottomgreen;
        image[0][j].rgbtBlue = bottomblue;
    }

    //top

    for (int j = 1; j < width - 1; j++)
    {
        float topredavg = (original[height - 1][j - 1].rgbtRed + original[height - 2][j - 1].rgbtRed + original[height - 1][j].rgbtRed +
                           original[height - 2][j].rgbtRed + original[height - 1][j + 1].rgbtRed + original[height - 2][j + 1].rgbtRed) / 6.0;
        int topred = round(topredavg);
        float topgreenavg = (original[height - 1][j - 1].rgbtGreen + original[height - 2][j - 1].rgbtGreen + original[height -
                             1][j].rgbtGreen + original[height - 2][j].rgbtGreen + original[height - 1][j + 1].rgbtGreen +
                             original[height - 2][j + 1].rgbtGreen) / 6.0;
        int topgreen = round(topgreenavg);
        float topblueavg = (original[height - 1][j - 1].rgbtBlue + original[height - 2][j - 1].rgbtBlue + original[height - 1][j].rgbtBlue +
                            original[height - 2][j].rgbtBlue + original[height - 1][j + 1].rgbtBlue + original[height - 2][j + 1].rgbtBlue) / 6.0;
        int topblue = round(topblueavg);

        image[height - 1][j].rgbtRed = topred;
        image[height - 1][j].rgbtGreen = topgreen;
        image[height - 1][j].rgbtBlue = topblue;
    }

    //left

    for (int i = 1; i < height - 1; i++)
    {
        float leftredavg = (original[i - 1][0].rgbtRed + original[i - 1][1].rgbtRed + original[i][0].rgbtRed + original[i][1].rgbtRed +
                            original[i + 1][0].rgbtRed + original[i + 1][1].rgbtRed) / 6.0;
        int leftred = round(leftredavg);
        float leftgreenavg = (original[i - 1][0].rgbtGreen + original[i - 1][1].rgbtGreen + original[i][0].rgbtGreen +
                              original[i][1].rgbtGreen + original[i + 1][0].rgbtGreen + original[i + 1][1].rgbtGreen) / 6.0;
        int leftgreen = round(leftgreenavg);
        float leftblueavg = (original[i - 1][0].rgbtBlue + original[i - 1][1].rgbtBlue + original[i][0].rgbtBlue + original[i][1].rgbtBlue +
                             original[i + 1][0].rgbtBlue + original[i + 1][1].rgbtBlue) / 6.0;
        int leftblue = round(leftblueavg);

        image[i][0].rgbtRed = leftred;
        image[i][0].rgbtGreen = leftgreen;
        image[i][0].rgbtBlue = leftblue;
    }

    //right

    for (int i = 1; i < height - 1; i++)
    {
        float rightredavg = (original[i - 1][width - 1].rgbtRed + original[i - 1][width - 2].rgbtRed + original[i][width - 1].rgbtRed +
                             original[i][width - 2].rgbtRed + original[i + 1][width - 1].rgbtRed + original[i + 1][width - 2].rgbtRed) / 6.0;
        int rightred = round(rightredavg);
        float rightgreenavg = (original[i - 1][width - 1].rgbtGreen + original[i - 1][width - 2].rgbtGreen + original[i]
                               [width - 1].rgbtGreen + original[i][width - 2].rgbtGreen + original[i + 1][width - 1].rgbtGreen +
                               original[i + 1][width - 2].rgbtGreen) / 6.0;
        int rightgreen = round(rightgreenavg);
        float rightblueavg = (original[i - 1][width - 1].rgbtBlue + original[i - 1][width - 2].rgbtBlue + original[i][width - 1].rgbtBlue +
                              original[i][width - 2].rgbtBlue + original[i + 1][width - 1].rgbtBlue + original[i + 1][width - 2].rgbtBlue) / 6.0;
        int rightblue = round(rightblueavg);

        image[i][width - 1].rgbtRed = rightred;
        image[i][width - 1].rgbtGreen = rightgreen;
        image[i][width - 1].rgbtBlue = rightblue;
    }

    //Mid pixels

    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            float midredavg = (original[i - 1][j - 1].rgbtRed + original[i - 1][j].rgbtRed + original[i - 1][j + 1].rgbtRed + original[i]
                               [j - 1].rgbtRed + original[i][j].rgbtRed + original[i][j + 1].rgbtRed + original[i + 1][j - 1].rgbtRed +
                               original[i + 1][j].rgbtRed + original[i + 1][j + 1].rgbtRed) / 9.0;
            int midred = round(midredavg);
            float midgreenavg = (original[i - 1][j - 1].rgbtGreen + original[i - 1][j].rgbtGreen + original[i - 1][j + 1].rgbtGreen +
                                 original[i][j - 1].rgbtGreen + original[i][j].rgbtGreen + original[i][j + 1].rgbtGreen + original[i + 1][j-1].rgbtGreen +
                                 original[i + 1][j].rgbtGreen + original[i + 1][j + 1].rgbtGreen) / 9.0;
            int midgreen = round(midgreenavg);
            float midblueavg = (original[i - 1][j - 1].rgbtBlue + original[i - 1][j].rgbtBlue + original[i - 1][j + 1].rgbtBlue +
                                original[i][j - 1].rgbtBlue + original[i][j].rgbtBlue + original[i][j + 1].rgbtBlue + original[i + 1][j - 1].rgbtBlue +
                                original[i + 1][j].rgbtBlue + original[i + 1][j + 1].rgbtBlue) / 9.0;
            int midblue = round(midblueavg);

            image[i][j].rgbtRed = midred;
            image[i][j].rgbtGreen = midgreen;
            image[i][j].rgbtBlue = midblue;
        }
    }
    return;
}
