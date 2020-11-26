// Problem set 1 : cash.c

#include <cs50.h>
#include <stdio.h>
#include <math.h>


int main(void)
{
    float price = 0.0;
    do
    {
       price = get_float("What's the price?\n$");
    } 
    while (price <= 0);

    printf("Your total is $%.2f.\n", price);

    int cents = price * 100;
    
    printf("%i\u00A2\n", cents);

    int quarters = cents / 25;
    
    if (quarters * 25 - cents  == 0)
    {
            int coins = (quarters);
            printf("There is %i coins", coins);
    }
    else
    {
        int r = (cents - quarters * 25);
        int dimes = (r / 10);

        if (r - dimes * 10 == 0)
        {
            int coins = (quarters + dimes);
            printf("There is %i coins", coins);
        }
        else
        {
            int r2 = (r - dimes * 10);
            int nickels = (r2 / 5);

            if(r2 - nickels * 5 == 0)
            {
                int coins = (quarters + dimes + nickels);
                printf("There is %i coins", coins);
            }
            else
            {
                int pennies = (r2 - nickels * 5);
                int coins = (quarters + dimes + nickels + pennies);
                printf("There is %i coins", coins);
            }
            
        }
        
    }
    
}
