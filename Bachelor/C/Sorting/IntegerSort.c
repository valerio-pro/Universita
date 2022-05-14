#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void IntegerSort(int[], int);

void IntegerSort(int a[], int n){         // T(n) = O(n+max)

    int i, j, max, *y;

    max = a[0];
    for(i = 1; i < n; i++){       // trovare il massimo in 'a' --> O(n)
        if(a[i] > max) max = a[i];
    }

    y = malloc(sizeof(int)*max);

    for(i = 0; i < max+1; i++){    // inizializzare il vettore 'y' --> O(max)
        y[i] = 0;
    }

    for(i = 0; i < n; i++){   // O(n)
        y[a[i]]++;      // all'i-esimo indice del vettore 'y', troviamo il numero di occorrenze del valore 'i' in 'a'
    }

    j = 0;
    for(i = 0; i < max+1; i++){  // O(n+max)
        while(y[i] > 0){
            a[j] = i;
            j++;
            y[i]--;
        }
    }

}

void main(){

    int i, n;
    printf("Inserisci la dimensione dell'array generato casualmente (valori pseudo-casuali tra 0 e 1024 incluso): ");
    scanf("%d", &n);
    int a[n];
    srand(time(NULL));

    for(i = 0; i < n; i++){
        a[i] = rand()%1024+1;
    }

    printf("Array generato: ");
    for(i = 0; i < n; i++){
        if(i != n-1) printf("%d, ", a[i]);
        else printf("%d\n", a[i]);
    }

    IntegerSort(a, n);

    printf("Array ordinato: ");
    for(i = 0; i < n; i++){
        if(i != n-1) printf("%d, ", a[i]);
        else printf("%d", a[i]);
    }

}
