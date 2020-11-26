// Problem set 1 : credit.c

#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // long credit = get_long("Enter credit card number: ");
    // printf("Credit card number is: %li\n", credit);

    long credit = 4530965425854712;

    long n1 = floor(credit * pow(10, -15));
    printf("1st number is: %li\n", n1 * 2);

    long n2 = floor(credit * pow(10, -13));
    long r = n2 % 10;
    printf("2nd number is: %li\n", r * 2);

    long n3 = floor(credit * pow(10, -11));
    long r1 = n3 % 10;
    printf("3rd number is: %li\n", r1 * 2);

    long n4 = floor(credit * pow(10, -9));
    long r2 = n4 % 10;
    printf("4th number is: %li\n", r2 * 2);

    long n5 = floor(credit * pow(10, -7));
    long r3 = n5 % 10;
    printf("5th number is: %li\n", r3 * 2);

    long n6 = floor(credit * pow(10, -5));
    long r4 = n6 % 10;
    printf("6th number is: %li\n", r4 * 2);

    long n7 = floor(credit * pow(10, -3));
    long r5 = n7 % 10;
    printf("7th number is: %li\n", r5 * 2);

    long n8 = floor(credit * pow(10, -1));
    long r6 = n8 % 10;
    printf("8th number is: %li\n", r6 * 2);

    // Sum of all digit numbers

    int d1 = (n1 * 2) % 10;
    int d2 = floor((n1 * 2) / 10);
    
    int d3 = (r * 2) % 10;
    int d4 = floor((r * 2) / 10);

    int d5 = (r1 * 2) % 10;
    int d6 = floor((r1 * 2) / 10);

    int d7 = (r2 * 2) % 10;
    int d8 = floor((r2 * 2) / 10);

    int d9 = (r3 * 2) % 10;
    int d10 = floor((r3 * 2) / 10);

    int d11 = (r4 * 2) % 10;
    int d12 = floor((r4 * 2) / 10);

    int d13 = (r5 * 2) % 10;
    int d14 = floor((r5 * 2) / 10);

    int d15 = (r6 * 2) % 10;
    int d16 = floor((r6 * 2) / 10);

    int i = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 + d15 + d16;

    // Numbers that not multiply

    long n11 = floor(credit * pow(10, -14));
    long r11 = n11 % 10;
    printf("1st number is: %li\n", r11);

    long n22 = floor(credit * pow(10, -12));
    long rr = n22 % 10;
    printf("2nd number is: %li\n", rr);

    long n33 = floor(credit * pow(10, -10));
    long rr1 = n33 % 10;
    printf("3rd number is: %li\n", rr1);

    long n44 = floor(credit * pow(10, -8));
    long rr2 = n44 % 10;
    printf("4th number is: %li\n", rr2);

    long n55 = floor(credit * pow(10, -6));
    long rr3 = n55 % 10;
    printf("5th number is: %li\n", rr3);

    long n66 = floor(credit * pow(10, -4));
    long rr4 = n66 % 10;
    printf("6th number is: %li\n", rr4);

    long n77 = floor(credit * pow(10, -2));
    long rr5 = n77 % 10;
    printf("7th number is: %li\n", rr5);

    long n88 = floor(credit * pow(10, 0));
    long rr6 = n88 % 10;
    printf("8th number is: %li\n", rr6);

    // add the sum (i) to the sum of digits that werent multiply then find the last number

    int j = (i + r11 + rr + rr1 + rr2 + rr3 + rr4 + rr5 + rr6) % 10;

    if (j == 0)
    {
        printf("VISA");
    }
    else
    {
        printf("INVALID");
    }
    
}