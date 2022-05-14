#include <stdio.h>
#include <stdlib.h>

struct nodo{
	int valore;
	struct nodo *succ;
	struct nodo *prec;
};
typedef struct nodo nodo;


nodo *ListaVuota();
nodo *ListaIn0(nodo *, int);
void ListaPrint(nodo *);
nodo *Reverse(nodo *);
nodo *ReverseThis(nodo *);


nodo *Reverse(nodo *head){

	if(head == NULL) return head;

	return ReverseThis(head);

}


nodo *ReverseThis(nodo *head){

	nodo *curr = head;
	nodo *tmp_next = curr->succ;
	nodo *tmp_prev = curr->prec;
	curr->succ = tmp_prev;
	curr->prec = tmp_next;
	if(tmp_next != NULL) return ReverseThis(tmp_next);
	else return head;

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
	n->prec = NULL;
	if(a != NULL)
		a->prec = n;
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
