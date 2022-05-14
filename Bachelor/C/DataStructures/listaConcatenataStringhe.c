#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

struct nodo {
	char *valore;
	struct nodo *succ;
	struct nodo *prec;
};
typedef struct nodo nodo;

nodo *ListaVuota();
nodo *ListaIn0(nodo *, char *);
nodo *ListaIn1(nodo *, char *);
nodo *ListaIn(nodo *, char *, int);
nodo *ListaOut0(nodo *);
nodo *ListaOut1(nodo *);
nodo *ListaOut(nodo *, int);
void ListaPrint(nodo *);
nodo *ListaSearch(nodo *, int);
nodo *ListaFromArray(char **, int);
nodo *ListaFromFile(char *);
int LunghezzaLista(nodo *);

void BubbleSort(nodo *);
nodo *ListaInSorted(nodo *, char *);

nodo *ListaInSorted(nodo *a, char *k){   // a e' una lista ordinata e la funzione inserisce l'elemento k 
                                         // nella posizione corretta per mantenere ordinamento
	nodo *p = a;

	if((p == NULL) || (strcmp(k, p->valore) < 0)){
		a = ListaIn0(a, k);
		return a;
	}

	while((p->succ != NULL) && (strcmp(k, p->succ->valore) > 0))
    	p = p->succ;

	if((p->succ == NULL) || (strcmp(k, p->succ->valore) <= 0))
    	p = ListaIn1(p, k);

	return a;

}

void BubbleSort(nodo *a){

    int finito = 0;
    char *t;
    nodo *j;
    while(finito == 0){
        finito = 1;
        for(j = a; j != NULL; j = j->succ){
            if(j->succ != NULL && (strcmp(j->valore, j->succ->valore) > 0)){
                finito = 0;
                t = j->succ->valore;
                j->succ->valore = j->valore;
                j->valore = t;
            }
        }
    }

}

int LunghezzaLista(nodo *a){

	int n = 1;
	while(a->succ != NULL){
		a = a->succ;
		n++;
	}

	return n;

}


/*
 * Restituisce una nuova lista vuota
 * */
nodo *ListaVuota(){
	return NULL;
}

/*
 * Aggiunge un nuovo nodo, con info v, in testa alla lista
 * */
nodo *ListaIn0(nodo *a, char *v){

	int lv = strlen(v);
	nodo *n = malloc(sizeof(nodo));
	n->valore = malloc((lv+1)*sizeof(char));
	strcpy(n->valore, v);
	n->succ = a;
	n->prec = NULL;
	if(a != NULL)
		a->prec = n;
	a = n;
	return a;

}

/*
 * Aggiunge un nuovo nodo, con info v, in pos 1 della lista
 * */
nodo *ListaIn1(nodo *p, char *v){

	nodo *n;
	int lv;
	if(p == NULL)
		return p;
	n = malloc(sizeof(nodo));
	lv = strlen(v);
	n->valore = malloc((lv+1)*sizeof(char));
	strcpy(n->valore, v);
	n->prec = p;
	n->succ = p->succ;
	if(p->succ != NULL)
		p->succ->prec = n;
	p->succ = n;
	return p;

}

/*
 * Inserisce nuovo nodo con info v  in posizione pos di a
 * 
 * */
nodo *ListaIn(nodo *a, char *v, int pos){

	nodo *p;
	if(pos < 0)
		return a;
	if(pos == 0)
		a = ListaIn0(a, v);
	else{
		p = ListaSearch(a, pos-1);
		if(p != NULL){
			p = ListaIn1(p, v);
		}
	}
	return a;

}

/*
 * Elimina il primo nodo dalla lista a
 * */
nodo *ListaOut0(nodo *a){

	nodo *p;
	if(a == NULL)
		return NULL;
	p = a->succ;
	if(p != NULL)
		p->prec = NULL;
	free(a->valore);     //NB: prima liberare l'array di char, DOPO il nodo
	free(a);
	a = p;

	return a;

}

/*
 * Elimina il secondo nodo dalla lista a
 * */
nodo *ListaOut1(nodo *p){

	nodo *q;
	if(p == NULL || p->succ == NULL)
		return p;
	q = p->succ->succ;
	free(p->succ->valore);
	free(p->succ);
	p->succ = q;
	if(q != NULL)
		q->prec = p;
		
	return p;
	
}

/*
 * Elimina il nodo in posizione pos dalla lista a
 * */
nodo *ListaOut(nodo *a, int pos){

	nodo *p;
	if(pos < 0)
		return a;
	if(pos == 0)
		a = ListaOut0(a);
	else{
		p = ListaSearch(a, pos-1);
		if(p != NULL){
			p = ListaOut1(p);
		}
	}

	return a;

}

/*
 * Restituisce l'indirizzo del nodo in posizione pos di a
 * oppure NULL se la lista non contiene tale nodo.
 * */
nodo *ListaSearch(nodo *a, int pos){

	nodo *p = a;
	int i = 0;
	while(i < pos && p != NULL){
		i++;
		p = p->succ;
	}

	return p;

}


/*
 * Stampa tutti gli elementi della lista.
 * */
void ListaPrint(nodo *a){

	nodo *p = a;
	while(p != NULL){
		printf("%s, ", p->valore);
		p = p->succ;
	}
	printf("\n");

}

/*
 *  b e' un array di dimensione n, la funzione restituisce una lista
 *  di n nodi contenenti gli interi di b rispettando l'ordinamento
 * 	in b. 
 * 
 * */
nodo *ListaFromArray(char *b[], int n){

	nodo *p, *a = ListaVuota();
	int i;
	for(i = 0; i < n; i++){
		if(a == NULL){
			a = ListaIn0(a, b[i]);
			p = a;
		}else{
			p = ListaIn1(p, b[i]);
			p = p->succ;
		}
	}

	return a;

}

/*
 *  filename e' il nome di un file di testo
 *  la funzione deve restituire la lista concatenata contenente le
 * 	parole (sequenze di lettere, no punteggiatura) del file.
 * 
 **/
nodo *ListaFromFile(char *filename){

	FILE *fp;
	char b[1000];
	int n = sizeof(b)/sizeof(char);
	int i, nr;
	char cword[20];
	int i_nw = 0;
	nodo *p, *a = ListaVuota();
	
	fp = fopen(filename, "r");
	if(fp == NULL){
		return a;
	}
	
	while((nr = fread(b, 1, n, fp)) != 0){
		i = 0;
		while(i < nr){
			if(isalpha(b[i])){    /* b[i] alfabetico */
				cword[i_nw] = tolower(b[i]);
				i_nw++;
			}else if(i_nw > 0){  /* b[i] e' altro e cword non vuota */
				cword[i_nw] = '\0';				
				if(a == NULL){
					a = ListaIn0(a, cword);
					p = a;
				}else{
					p = ListaIn1(p, cword);
					p = p->succ;
				}			
				i_nw = 0;	
			}
			i++;
		}
	}

	fclose(fp);
	return a;

}



void main(int n, char *args[]){

	int i;
	char ins[100];
    
	nodo *a = ListaFromArray(args, n);
	ListaPrint(a);

	for(i = 0; i < 3; i++){
		a = ListaOut0(a);
	}
	ListaPrint(a);
	
}
