#include <stdio.h>
#include <stdlib.h>

void MergeSort(int [], int, int);
void Merge(int [], int, int, int);

void Merge(int a[], int low, int m, int high){

    int i = low, j = m+1, k = 0;
    int tmp[high-low+1];

    while(i <= m && j <= high){
        if(a[i] <= a[j]){
            tmp[k] = a[i];
            i++;
        }
        else{
            tmp[k] = a[j];
            j++; 
        }
        k++;
    }

    while(i <= m){
        tmp[k] = a[i]; i++; k++;
    }
    while(j <= high){
        tmp[k] = a[j]; j++; k++;
    }

    for(k = low; k <= high; k++){
        a[k] = tmp[k-low];
    }

}

void MergeSort(int a[], int low, int high){

    int m;

    if(low < high){
        m = ((low+high)/2);
        MergeSort(a, low, m);
        MergeSort(a, m+1, high);
        Merge(a, low, m, high);
    }

}

void main(){

    int a[] = {1, 2, 1, 345, 123, 131, 1231, 2, 3, 12};
    int n = sizeof(a)/sizeof(int);
    int i;

    for(i = 0; i < n; i++){
        printf("%d, ", a[i]);
    } printf("\n");

    MergeSort(a, 0, n-1);

    for(i = 0; i < n; i++){
        printf("%d, ", a[i]);
    }

}
