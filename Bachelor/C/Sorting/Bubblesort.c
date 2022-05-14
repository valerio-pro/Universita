// Algoritmo di BubbleSort ottimizzato//
// N.B: ci sono 3 versioni del BubbleSort, l'ultima è la più ottimizzata, anche se tutte hanno lo stesso costo di n*n operazioni

#include <stdio.h>
#include <string.h>


void BubbleSort0(char[]);
void BubbleSort1(char[]);
void BubbleSort(char[]);



void main(){
	
	char a[] = "programmazione";

	BubbleSort(a);
	
	printf("%s\n", a);
	
}

void BubbleSort0(char b[]){
	
	int n = strlen(b); /* circa n operazioni */
	int i, j; 
	char c;
	
	/*   circa n*n operazioni  */
	for (i = 0;  i < n-1; i = i+1){
		for(j = 0; j < n-1; j = j+1){
		    if(b[j] > b[j+1]){         /* test if eseguito (n-1)*(n-1) volte ovvero circa n*2 volte */
				c = b[j];
				b[j] = b[j+1];
				b[j+1] = c;
			}
		}
	}
	
	/*
	 * Numero totale di operazioni:
	 * 
	 * n + n*n = circa n*n
	 * 
	 * algoritmo di costo quadratico nella grandezza dell'input
	 * 
	 * */
	
}

void BubbleSort1(char b[]){     //modello preferito//
	
	int n = strlen(b); /* circa n operazioni */
	int i, j; 
	char c;
	
	/*   circa n*n operazioni  */
	for(i = 0;  i < n-1; i = i+1){
		for(j = 0; j < n-1-i; j = j+1){
			if(b[j] > b[j+1]){               /* test if eseguito (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2*/
		        c = b[j];
				b[j] = b[j+1];
				b[j+1] = c;
			}
		}
	}                                             	                     	                                              		 		                                                                               
	
	/*
	 * Numero totale di operazioni:
	 * 
	 * n+n(n-1)/2 = circa n*n
	 * 
	 * algoritmo costo quadratico nella grandezza dell'input
	 * 
	 * */
	
}

void BubbleSort(char b[]){
	
	int n = strlen(b); /* circa n operazioni */
	int i, j; 
	char c;
	int ordinato = 0;
	
	/* circa n*n operazioni nel caso peggiore */
	i = 0;
	while (ordinato == 0){          //introduco la variabile "ordinato"//
		ordinato = 1;                 //scommetto che la sequenza è ordinata così se non è ordinata entra nell'IF//
		for(j = 0; j < n-1-i; j = j+1){
			if(b[j] > b[j+1]){              /* test if eseguito nel caso peggiore (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2 */
				c = b[j];
				b[j] = b[j+1];
				b[j+1] = c;
				ordinato = 0;
			}
		}
		i = i+1;
	}
	
	/*
	 * Numero totale di operazioni nel caso peggiore:
	 * 
	 *n(n-1)/2 = n*n
	 * 
	 * algoritmo nel caso peggiore ha costo
	 * quadratico nella grandezza dell'input
	 * 
	 * */
	
}
