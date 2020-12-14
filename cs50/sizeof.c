#include <stdio.h> 
int main() 
{ 
    int data[] = {-2, 45, 0, 11, -9};
    int d1 = sizeof(data[0]);
    int len_array = sizeof(data) / d1;
    printf("size of a char type variable is: %lu bytes\n", sizeof(char)); 
    printf("size of a int type variable is: %lu bytes\n", sizeof(int)); 
    printf("size of a float type variable is: %lu bytes\n", sizeof(float)); 
    printf("size of a double type variable is: %lu bytes\n\n", sizeof(double));
    printf("size of array data is : %lu bytes\n", sizeof(data));
    printf("divided by:\n");
    printf("size of 1st number in data is: %lu bytes\n", sizeof(d1));
    printf("equals to:\n");
    printf("Lenght of array 'data': %i items\n", len_array); 
    return 0;
}