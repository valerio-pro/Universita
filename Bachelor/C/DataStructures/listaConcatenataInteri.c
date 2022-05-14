#include <stdlib.h>
#include <stdio.h>

struct nodo{
	int valore;
	struct nodo *succ;
	struct nodo *prec;
};
typedef struct nodo nodo;

nodo *ListaVuota();
nodo *ListaIn0(nodo *, int);
nodo *ListaIn1(nodo *, int);
nodo *ListaIn(nodo *, int, int);
nodo *ListaOut0(nodo *);
nodo *ListaOut1(nodo *);
nodo *ListaOut(nodo *, int);
void ListaPrint(nodo *);
nodo *ListaSearch(nodo *, int);
nodo *ListaAppend(nodo *, int);
nodo *ListaFromArray(int *, int);
nodo *ListaRaddoppia(nodo *);
int LunghezzaLista(nodo *);


nodo *ListaInverti(nodo *);
void BubbleSort(nodo *);
nodo *ListaInSorted(nodo *, int);

nodo *ListaInverti(nodo *a){

	nodo *b, *p;
	b = ListaVuota();

	while(a != NULL){
		p = a->succ;
		a->succ = b;
		if(b != NULL)
			b->prec = a;
		a->prec = NULL;
		b = a;
		a = p;
	}
	return b;

}

nodo *ListaInSorted(nodo *a, int k){   // a e' una lista ordinata e la funzione inserisce l'elemento k 
									   // nella posizione corretta per mantenere ordinamento
	nodo *p = a;

	if((p == NULL) || (k < p->valore)){
		a = ListaIn0(a, k);
		return a;
	}

	while((p->succ != NULL) && (p->succ->valore < k))
    	p = p->succ;

	if((p->succ == NULL) || (p->succ->valore >= k))
   		p = ListaIn1(p, k);

	return a;

}

void BubbleSort(nodo *a){

    int finito = 0;
    int t;
    nodo *j;
    while(finito == 0){
        finito = 1;
        for(j = a; j != NULL; j = j->succ){
            if(j->succ != NULL && (j->valore > j->succ->valore)){
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
nodo *ListaIn0(nodo *a, int v){

	nodo *n = malloc(sizeof(nodo));
	n->valore = v;
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
nodo *ListaIn1(nodo *p, int v){

	nodo *n;
	if(p == NULL)
		return p;
	n = malloc(sizeof(nodo));
	n->valore = v;
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
nodo *ListaIn(nodo *a, int v, int pos){

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

	if(a == NULL)
		return NULL;
	nodo *p = a->succ;
	if(p != NULL)
		p->prec = NULL;
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
		printf("%d, ", p->valore);
		p = p->succ;
	}
	printf("\n");

}


/*
 * Inserisce un nuovo nodo in fondo alla lista a
 * */
nodo *ListaAppend(nodo *a, int v){

	nodo *p = a;
	if(a == NULL)
		a = ListaIn0(a,v);
	else{
		while(p->succ != NULL)
			p = p->succ;
		p = ListaIn1(p, v);
	}

	return a;

}

/*
 *  b e' un array di dimensione n, la funzione restituisce una lista
 *  di n nodi contenenti gli interi di b rispettando l'ordinamento
 * 	in b. 
 * 
 * */
nodo *ListaFromArray(int *b, int n){

	nodo *p, *a = ListaVuota();
	int i;

	for(i = 0; i < n; i++){
		if (a == NULL){
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
 *  filename e' il nome di un file di testo csv con una unica colonna
 * 	di interi separati da ;
 *  la funzione deve restituire la lista concatenata contenente gli
 *  interi nel file.
 * 
 * */
nodo *ListaFromFile(char *filename){

	FILE *fpin;
	int n;
	fpin = fopen(filename, "r");
	nodo  *p, *a = ListaVuota();
	
	if(fpin == NULL){
		printf("Errore apertura file\n");
		return NULL;
	}
	
	while(feof(fpin) == 0){  /* non siamo alla fine del file */
		if(fscanf(fpin, "%d;", &n) == 1){
			/*
			 * Aggiungere n in fondo alla lista
			 * */
			if(a == NULL){
				a = ListaIn0(a, n);
				p = a;
			}else{
				p = ListaIn1(p, n);
				p = p->succ;
			}
		}
	}
	
	fclose(fpin);
	return a;

}

/*
 * Sia n la lunghezza di a, aggiunge ad a n+1 nodi  con valore zero
 * in fondo alla lista.
 * */
nodo *ListaRaddoppia(nodo *a){

	nodo *p = a;
	int i, n = 1;
	
	if(a == NULL)
		return ListaIn0(NULL, 0);
	
	while(p->succ != NULL){
		p = p->succ;
		n++;
	}
	
	for(i = 0; i < n+1; i++){
		p = ListaIn1(p, 0);
	}
	
	return a;

}


void main(){

	int i;
	int b[] = {10, 20, 30, 40};
	int n = sizeof(b)/sizeof(int);

	nodo *a = ListaFromArray(b, n);
	ListaPrint(a);

	nodo *aa = ListaFromFile("25-interi.csv");
	ListaPrint(aa);
	
	aa = ListaRaddoppia(aa);
	ListaPrint(aa);
	
}
