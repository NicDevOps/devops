#include "helpers.h"
#include <math.h>
#include <stdlib.h>

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
            // image[i][j].rgbtRed = avg_red;
        }
    }
}


void edges(int height, int width, RGBTRIPLE image[height][width])
{
   
    int gx[3][3] = {{-1, 0, 1},
                    {-2, 0, 2},
                    {-1, 0, 1}};

    int gy[3][3] = {{-1, -2, -1},
                    {0, 0, 0},
                    {1, 2, 1}};

    RGBTRIPLE(*buffer)[width] = calloc(height, width * sizeof(RGBTRIPLE));


    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            // buffer[i][j].rgbtRed = 255;
            // buffer[i][j].rgbtGreen = 0;
            // buffer[i][j].rgbtBlue = 0;
            int sum_red_gx = 0;
            int sum_green_gx = 0;
            int sum_blue_gx = 0;
            int sum_red_gy = 0;
            int sum_green_gy = 0;
            int sum_blue_gy = 0;

            for (int x = 0; x < 3; x++)
            {
                for (int y = 0; y < 3; y++)
                {
                    int nx = x - 1 + i;
                    int ny = y - 1 + j;
                    sum_red_gx = sum_red_gx + image[nx][ny].rgbtRed * gx[x][y];
                    sum_green_gx = sum_green_gx + image[nx][ny].rgbtGreen * gx[x][y];
                    sum_blue_gx = sum_blue_gx + image[nx][ny].rgbtBlue * gx[x][y];
                    sum_red_gy = sum_red_gy + image[nx][ny].rgbtRed * gy[x][y];
                    sum_green_gy = sum_green_gy + image[nx][ny].rgbtGreen * gy[x][y];
                    sum_blue_gy = sum_blue_gy + image[nx][ny].rgbtBlue * gy[x][y];
                }
            }

            int delta_red = (int)round(sqrt(sum_red_gx * sum_red_gx + sum_red_gy * sum_red_gy));
            int delta_green = (int)round(sqrt(sum_green_gx * sum_green_gx + sum_green_gy * sum_green_gy));
            int delta_blue = (int)round(sqrt(sum_blue_gx * sum_blue_gx + sum_blue_gy * sum_blue_gy));

            if (delta_red > 255)
            {
                delta_red = 255;
            }
            if (delta_green > 255)
            {
                delta_green = 255;
            }
            if (delta_blue > 255)
            {
                delta_blue = 255;
            }
            buffer[i][j].rgbtRed = delta_red;
            buffer[i][j].rgbtGreen = delta_green;
            buffer[i][j].rgbtBlue = delta_blue;
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = buffer[i][j].rgbtRed;
            image[i][j].rgbtGreen = buffer[i][j].rgbtGreen;
            image[i][j].rgbtBlue = buffer[i][j].rgbtBlue;
        }
    }
    free(buffer);
}


void heatmap(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE *palette = malloc(255 * sizeof(RGBTRIPLE));

    for (int i = 0; i < 256; i++)
    {
        int step = i % 4;
        palette[i].rgbtRed = step * 4;
        palette[i].rgbtGreen = 0;
        palette[i].rgbtBlue = 0;    
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int index = image[i][j].rgbtRed;
            RGBTRIPLE color = palette[index];
            image[i][j].rgbtRed = color.rgbtRed;
            // image[i][j].rgbtGreen = color.rgbtGreen;
            // image[i][j].rgbtBlue = color.rgbtBlue;
        }
    }

    free(palette);
}
