#include <stdio.h>

void main(){
                         // Successione:  F = Fp + Fpp, si assume che F0 = 0 e F1 = 1
	int n;
	int i = 2;
	int Fp = 1;     // Fp := fibo. prec.
	int Fpp = 0;    // Fpp := fibo. prec. prec.
	int F;

	printf("inserisci un valore numerico\n");
	scanf("%d", &n);            // per lo scan di interi si usa "%d"
	
	if(n >= 2){
		while(i <= n){  
			F = Fp + Fpp;
			Fpp = Fp;
			Fp = F;
			i++;
	        }
	
        }
	
	else{ F = n; }  // F0 = 0 e F1 = 1 

    printf("%d\n", F);  // per printare interi si usa "%d\n" 

} 
