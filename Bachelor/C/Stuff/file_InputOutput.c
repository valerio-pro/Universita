#include <stdio.h>

void MostraFile_getc(FILE *fp){

	char c;
	int n = 0;
	while((c = getc(fp)) != EOF){
		printf("%c", c);
		// n++; 
	}
	// printf("%d\n", n); 

}

void MostraFile_fgets(FILE *fp){

	char b[100];
	int n = 100;
	int l = 0;
	while(fgets(b, n, fp) != NULL){
		printf("%s", b);
		// l++;
	}
	// printf("%d\n", l); 

}

void MostraFile_fread(FILE *fp){

	char b[100];
	int n = 100;
	int nr;
	int l = 0;
	
	while((nr = fread(b, sizeof(char), n-1, fp)) != 0){  // al posto di "sizeof(char)" potevo mettere anche "1" direttamente //
		b[nr] = '\0';
		printf("%s", b);            // N.B: quando "fread()==0" allora la lettura del file e' terminata //
		// l++; 
	}
	// printf("%d\n", l); 

}

void FileStats(FILE *fp){

	char b[1000];
	int n = 1000;
	int numrows = 0;
	int numwords = 0;
	int numchars = 0;
	int i, nr;
	
	while((nr = fread( b, 1, n-1, fp)) != 0){
		numchars += nr;
		i = 0;
		while(i < nr){
			if(b[i] == ' ')
				numwords++;
			else if(b[i] == '\n'){
				numrows++;
				numwords++;
			}
			i++;
		}
	}
	printf("%d, %d, %d\n", numrows, numwords, numchars);

}

void main(){

	FILE *fpin;
	fpin = fopen("file.c", "r");

	if(fpin == NULL){
		printf("Errore di apertura\n");
		return;
	}

	FileStats(fpin); 
	fclose(fpin);

}
