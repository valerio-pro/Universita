#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

void Scambia(int *a, int x, int y){

	int t = a[x];
	a[x] = a[y];
	a[y] = t;

}

int Distribuzione(int *a, int sx, int dx){  // L'algoritmo di Distribuzione ha costo lineare //

	int p;
	int i = sx+1, j = dx;
	int finale = sx;
	
	srand(time(NULL));   /* init seed */
	p = (rand() % (dx-sx+1)) + sx;   /* un numero tra sx e dx*/
	Scambia(a, sx, p);
	
	while(i <= j){
		while(i <= j && a[i] <= a[sx]){
			finale = i;
			i++;
		}
		while(i <= j && a[j] > a[sx]){
			j--;
		}
		if(i <= j)
			Scambia(a, i, j);
	}
	Scambia(a, sx, finale);
	
	return finale;

}

void QuickSort(int *a, int sx, int dx){  // Nella maggior parte dei casi ha costo pari a nLog(n) //
                                         // Nel caso peggiore ha costo quadratico ma e' molto improbabile //
	int posizione_pivot;
	if(sx <= dx){
		posizione_pivot = Distribuzione(a, sx, dx);
		QuickSort(a, sx, posizione_pivot - 1);
		QuickSort(a, posizione_pivot + 1, dx);
	}

} 

void main(){

	int a[] = {5, 1, 2, 6, 5, 4, 3, 2, 1, 8, 5, 3, 1, 6, 9};
	int i, n = sizeof(a)/sizeof(int);
	QuickSort(a, 0, n-1);
	for(i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");

}
