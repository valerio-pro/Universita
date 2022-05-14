#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

struct chiave_valore{
	char *k;
	int v;
};
typedef struct chiave_valore chiave_valore; 

struct nodo{
	chiave_valore valore;
	struct nodo *succ;
	struct nodo *prec;
};
typedef struct nodo nodo;

struct dizionario{
	int m;          // m e' il numero di liste di cui e' composto il dizionario 
	nodo **array;
};
typedef struct dizionario dizionario;

dizionario DizionarioVuoto(int);
dizionario DizionarioIn(dizionario, chiave_valore);
dizionario DizionarioCanc(dizionario, char *);
void DizionarioPrint(dizionario);
nodo *DizionarioSearch(dizionario, char *);
int DizionarioTest(dizionario, char *);
int DizionarioGet(dizionario, char *);

int h(char *, int);   // Funzione hash 

nodo *ListaVuota();
nodo *ListaIn0(nodo*, chiave_valore);

/*
 * Restituisce un dizionario vuoto
 * */
dizionario DizionarioVuoto(int m){

	dizionario d;
	int i;
	d.m = m;
	
	d.array = malloc(sizeof(nodo *)*m);
	
	for(i = 0; i < m; i++)
		d.array[i] = ListaVuota();
	
	return d;

}

/*
 * Definizione funzione hash, h = Resto(r/m) dove "m" e' il numero di liste di trabocco ed "r" e' la stringa "k" di input normalizzata in intero
 *
 * */
 int h(char *k, int m){    

	int i, r = 0;
	
	i = 0;
	while(k[i] != '\0'){
		r = r^k[i];        // "^" e' l'operatore xor, esegue lo xor bit a bit degli operandi
		i++;
	}
	
	return r%m;   // valore compreso tra 0 e m-1

 }

/*
 * Restituisce il puntatore al nodo contenente la coppia
 * con chiave k, NULL se tale coppia non esiste.
 * */
nodo *DizionarioSearch(dizionario d, char *k){

	nodo *p;
	
	p = d.array[h(k, d.m)];
	while(p != NULL){
		if(strcmp(p->valore.k, k) == 0)
			return p;
		p = p->succ;
	}
	
	return NULL;

}

/*
 * Restituisce 1 se k appartiene al dizionario d, 0 altrimenti
 * */
int DizionarioTest(dizionario d, char *k){

	if(DizionarioSearch(d, k) != NULL)
		return 1;
	else
		return 0;

}

/*
 * Restituisce il valore associato alla chiave k
 * 
 * Pre. k e' una chiave del dizionario.
 * 
 * */
int DizionarioGet(dizionario d, char *k){

	nodo *p = DizionarioSearch(d, k);
	
	return p->valore.v;

}


/*
 * Aggiunge al dizionario una nuova coppia kv se la chiave
 * kv.k non e' presente nel dizionario, altrimenti 
 * ne aggiorna il valore con quello di kv.v.
 * 
 * */
dizionario DizionarioIn(dizionario d, chiave_valore kv){

	nodo *p = DizionarioSearch(d, kv.k);
	
	if(p != NULL)
		p->valore.v = kv.v;
	else{
		d.array[h(kv.k, d.m)] = ListaIn0(d.array[h(kv.k, d.m)], kv);
	}
	
	return d;

}

/*
 * Restituisce la lista vuota
 * */
nodo *ListaVuota(){
	return NULL;
}


/*
 * Aggiunge un nuovo nodo, con info v, in testa alla lista
 * */
nodo *ListaIn0(nodo *a, chiave_valore v){

	int lk;
	nodo *n = malloc(sizeof(nodo));
	lk = strlen(v.k);
	
	n->valore.k = malloc((lk+1)*sizeof(char));
	strcpy(n->valore.k, v.k);
	n->valore.v = v.v;
	
	n->succ = a;
	n->prec = NULL;
	if(a != NULL)
		a->prec = n;
	a = n;
	
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
	free(a->valore.k);
	free(a);
	a = p;
	
	return a;

}

/*
 * Elimina il secondo nodo dalla lista p
 * */
nodo *ListaOut1(nodo *p){

	nodo *q;
	if(p == NULL || p->succ == NULL)
		return p;
	q = p->succ->succ;
	free(p->succ->valore.k);
	free(p->succ);
	p->succ = q;
	if(q != NULL)
		q->prec = p;
	
	return p;

}

/*
 * Elimina dal dizionario il nodo contenente la coppia con chiave k.
 * Restituisce il dizionario modificato. Se tale nodo non esiste
 * la funzione restituisce il dizionario non modificato.
 * 
 * */


 dizionario DizionarioCanc(dizionario d, char *k){

	nodo *p = DizionarioSearch(d, k);
	
	if(p != NULL){
		if(p == d.array[h(k, d.m)]){
			  d.array[h(k, d.m)] = ListaOut0(p);
		}else{
			  p = p->prec;
			  p = ListaOut1(p);
		}
	}
	
	return d;

 }
 

/*
 * Stampa tutti gli elementi del dizionario.
 * */
void DizionarioPrint(dizionario d){

	nodo *p;
	int i;
	
	for(i = 0; i < d.m; i++){
		p = d.array[i];
		printf("d.array[%d] = ", i);
		while(p != NULL){
			printf("%s: %d, ", p->valore.k, p->valore.v);
			p = p->succ;
		}
		printf("\n");
	}

}



/*
 * Crea un dizionario contenente coppie (k, v) dove k e' una 
 * parola nel file resa minuscola e v e' il numero di occorrenze di
 * v nel file.
 * 
 * Per parola si intende una sequenze di lettere.
 * 
 * Restituisce il dizionario creato.
 * 
 * */
dizionario ContaOccorrenze(char *filename){

	FILE *fp;
	char b[1000];
	int n = sizeof(b)/sizeof(char);
	int i, nr;
	char cword[20];
	int i_nw = 0;
	nodo *p;
	dizionario d = DizionarioVuoto(3);
	chiave_valore kv;
	
	fp = fopen(filename, "r");
	if(fp == NULL){
			return d;
	}
	
	while((nr = fread(b, 1, n, fp)) != 0){
		i = 0;
		while(i < nr){
			if(isalpha(b[i])){ /* b[i] alfabetico */
				cword[i_nw] = tolower(b[i]);
				i_nw++;
			}else if(i_nw > 0){ /* b[i] e' altro e cword non vuota*/
				cword[i_nw] = '\0';
				
				kv.k = cword;
				if(DizionarioTest(d, kv.k ) == 0){
					kv.v = 1;
				}else{
					/*
					 * La chiave e' nel dizionario
					 * */
					 kv.v = DizionarioGet(d, kv.k) + 1;
				}
				
				d = DizionarioIn(d, kv);		
				
				i_nw = 0;	
			}
			i++;
		}
	}
	
	fclose(fp);
	return d;

}

void main(int n, char *args[]){

	dizionario d = ContaOccorrenze("prova.txt");
    
	DizionarioPrint(d);
	d = DizionarioCanc(d, "molto");
	DizionarioPrint(d);
	
}
