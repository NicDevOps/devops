#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3);
            average = (int)average;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
       for (int j = 0; j < width; j++)
       {
            float sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            float sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            float sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            sepiaRed = (int)sepiaRed;
            sepiaGreen = (int)sepiaGreen;
            sepiaBlue = (int)sepiaBlue;

            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaRed;
            }
            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = sepiaGreen;
            }

            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = sepiaBlue;
            }
       } 
    }
}

// Unsigned integer swap function
void swap(uint8_t *a, uint8_t *b)
{
    uint8_t tmp = *a;
    *a = *b;
    *b = tmp;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][width - j].rgbtBlue, &image[i][j].rgbtBlue);
            swap(&image[i][width - j].rgbtGreen, &image[i][j].rgbtGreen);
            swap(&image[i][width - j].rgbtRed, &image[i][j].rgbtRed);
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            float avg_blue = round((image[i - 1][j - 1].rgbtBlue + image[i - 1][j + 0].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i + 0][j - 1].rgbtBlue + image[i + 0][j + 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i + 1][j + 0].rgbtBlue + image[i + 1][j + 1].rgbtBlue) / 8);
            avg_blue = (int)avg_blue;

            float avg_green = round((image[i - 1][j - 1].rgbtGreen + image[i - 1][j + 0].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i + 0][j - 1].rgbtGreen + image[i + 0][j + 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i + 1][j + 0].rgbtGreen + image[i + 1][j + 1].rgbtGreen) / 8);
            avg_green = (int)avg_green;

            float avg_red = round((image[i - 1][j - 1].rgbtRed + image[i - 1][j + 0].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i + 0][j - 1].rgbtRed + image[i + 0][j + 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i + 1][j + 0].rgbtRed + image[i + 1][j + 1].rgbtRed) / 8);
            avg_red = (int)avg_red;

            image[i][j].rgbtBlue = avg_blue;
            image[i][j].rgbtGreen = avg_green;
            image[i][j].rgbtRed = avg_red;
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            int xb1 = image[i - 1][j - 1].rgbtBlue * -1;
            int xb2 = image[i - 1][j + 0].rgbtBlue * 0;
            int xb3 = image[i - 1][j + 1].rgbtBlue * 1;
            int xb4 = image[i + 0][j - 1].rgbtBlue * -2;
            int xb5 = image[i + 0][j + 1].rgbtBlue * 2;
            int xb6 = image[i + 1][j - 1].rgbtBlue * -1;
            int xb7 = image[i + 1][j + 0].rgbtBlue * 0;
            int xb8 = image[i + 1][j + 1].rgbtBlue * 1;

            int xg1 = image[i - 1][j - 1].rgbtGreen * -1;
            int xg2 = image[i - 1][j + 0].rgbtGreen * 0;
            int xg3 = image[i - 1][j + 1].rgbtGreen * 1;
            int xg4 = image[i + 0][j - 1].rgbtGreen * -2;
            int xg5 = image[i + 0][j + 1].rgbtGreen * 2;
            int xg6 = image[i + 1][j - 1].rgbtGreen * -1;
            int xg7 = image[i + 1][j + 0].rgbtGreen * 0;
            int xg8 = image[i + 1][j + 1].rgbtGreen * 1;

            int xr1 = image[i - 1][j - 1].rgbtRed * -1;
            int xr2 = image[i - 1][j + 0].rgbtRed * 0;
            int xr3 = image[i - 1][j + 1].rgbtRed * 1;
            int xr4 = image[i + 0][j - 1].rgbtRed * -2;
            int xr5 = image[i + 0][j + 1].rgbtRed * 2;
            int xr6 = image[i + 1][j - 1].rgbtRed * -1;
            int xr7 = image[i + 1][j + 0].rgbtRed * 0;
            int xr8 = image[i + 1][j + 1].rgbtRed * 1;

            int yb1 = image[i - 1][j - 1].rgbtBlue * -1;
            int yb2 = image[i - 1][j + 0].rgbtBlue * -2;
            int yb3 = image[i - 1][j + 1].rgbtBlue * -1;
            int yb4 = image[i + 0][j - 1].rgbtBlue * 0;
            int yb5 = image[i + 0][j + 1].rgbtBlue * 0;
            int yb6 = image[i + 1][j - 1].rgbtBlue * 1;
            int yb7 = image[i + 1][j + 0].rgbtBlue * 2;
            int yb8 = image[i + 1][j + 1].rgbtBlue * 1;

            int yg1 = image[i - 1][j - 1].rgbtGreen * -1;
            int yg2 = image[i - 1][j + 0].rgbtGreen * -2;
            int yg3 = image[i - 1][j + 1].rgbtGreen * -1;
            int yg4 = image[i + 0][j - 1].rgbtGreen * -0;
            int yg5 = image[i + 0][j + 1].rgbtGreen * 0;
            int yg6 = image[i + 1][j - 1].rgbtGreen * 1;
            int yg7 = image[i + 1][j + 0].rgbtGreen * 2;
            int yg8 = image[i + 1][j + 1].rgbtGreen * 1;

            int yr1 = image[i - 1][j - 1].rgbtRed * -1;
            int yr2 = image[i - 1][j + 0].rgbtRed * -2;
            int yr3 = image[i - 1][j + 1].rgbtRed * -1;
            int yr4 = image[i + 0][j - 1].rgbtRed * 0;
            int yr5 = image[i + 0][j + 1].rgbtRed * 0;
            int yr6 = image[i + 1][j - 1].rgbtRed * 1;
            int yr7 = image[i + 1][j + 0].rgbtRed * 2;
            int yr8 = image[i + 1][j + 1].rgbtRed * 1;

            double Gx_blue = pow((xb1 + xb2 + xb3 + xb4 + xb5 + xb6 + xb7 + xb8), 2);
            double Gx_green = pow((xg1 + xg2 + xg3 + xg4 + xg5 + xg6 + xg7 + xg8), 2);
            double Gx_red = pow((xr1 + xr2 + xr3 + xr4 + xr5 + xr6 + xr7 + xr8), 2);

            double Gy_blue = pow((yb1 + yb2 + yb3 + yb4 + yb5 + yb6 + yb7 + yb8), 2);
            double Gy_green = pow((yg1 + yg2 + yg3 + yg4 + yg5 + yg6 + yg7 + yg8), 2);
            double Gy_red = pow((yr1 + yr2 + yr3 + yr4 + yr5 + yr6 + yr7 + yr8), 2);

            float blue = round(sqrt(Gx_blue + Gy_blue));
            float green = round(sqrt(Gx_green + Gy_green));
            float red = round(sqrt(Gx_red + Gy_red));

            blue = (int)blue;
            green = (int)green;
            red = (int)red;

            if (red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = red;
            }
            if (green > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = green;
            }

            if (blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = blue;
            }
        }
    }
}
