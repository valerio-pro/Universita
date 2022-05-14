#include <stdio.h>

int RicercaBinaria(int[], int, int, int);

void main(){
	
	int a[] = {0, 0, 1, 4, 6, 10, 11, 15, 17, 21, 23, 24, 24, 30, 36, 36};
	int n = sizeof(a)/sizeof(int);
	
	printf("%d\n", RicercaBinaria(a, 14, 0, n-1));
}

/*
 * 
 * a e' ordinato e di dimensione n
 * 
 * restituisce i se a[i] = k altrimenti -1
 * 
 * cerco k tra a[lx] e a[rx]
 * 
 * */

int RicercaBinaria(int a[], int k, int lx, int rx){
	
	int cx;
	
	if(lx > rx) return -1;
	
	cx = (rx+lx)/2;

	if(a[cx] == k) return cx;
		
	if (k < a[cx]) return RicercaBinaria(a, k, lx, cx-1);
	else return RicercaBinaria(a, k, cx+1, rx);
	
}
