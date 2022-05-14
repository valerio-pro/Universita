#include <stdio.h>
#include <stdlib.h>

struct nodo{
	int valore;
	struct nodo *succ;
};
typedef struct nodo nodo;


nodo *ListaVuota();
nodo *ListaIn0(nodo *, int);
void ListaPrint(nodo *);
nodo *ReverseThis(nodo *, nodo *);
nodo *Reverse(nodo *);

nodo *Reverse(nodo *head){

	return ReverseThis(head, NULL);

}

nodo *ReverseThis(nodo *head, nodo *previous){

	if(head != NULL){
		nodo *curr = head;
		nodo *tmp_next = curr->succ;
		curr->succ = previous;
		return ReverseThis(tmp_next, curr);
	}

	return previous;

}

void ListaPrint(nodo *a){

	nodo *p = a;
	while(p != NULL){
		if(p->succ != NULL) printf("%d, ", p->valore);
		else printf("%d", p->valore);
		p = p->succ;
	}
	printf("\n");

}

nodo *ListaIn0(nodo *a, int v){

	nodo *n = malloc(sizeof(nodo));
	n->valore = v;
	n->succ = a;
	a = n;
	return a;

}

nodo *ListaVuota(){
	return NULL;
}

void main(){

	nodo *a = ListaVuota();

    	for(int i = 20; i > 0; i--){
        	a = ListaIn0(a, i);
    	}
	
    	ListaPrint(a);

	nodo *r = Reverse(a);
	ListaPrint(r);

}
