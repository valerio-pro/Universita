#include <stdio.h>
#include <stdlib.h>

void main(){

	int n = 5;
	int *x = malloc(sizeof(int)*n);

	for(int i = 0; i < n; i++)
		*(x+i) = i+10;

	for(int i = 0; i < n; i++)
		printf("%p -> %d\n", x+i, *(x+i));

	exit(1);

}
