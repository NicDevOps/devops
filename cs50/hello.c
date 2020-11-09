#include <stdio.h>
#include "cs50.h"


int adderFunction(int a, int b)
{
	return a + b;
}

int main()
{
	printf("2333322----------\n");
	int x = get_int("x: ");
	int result = adderFunction(11, 222);

	printf("result: %d\n", result);
}

