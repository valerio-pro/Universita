#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// enum definisce un tipo enumerativo basato su costanti
typedef enum {false = 0, true = 1} boolean;  // Definizione tipo booleano


struct tnode{           
    char *element;
    int key;         
    struct tnode *left, *right, *parent;
};
typedef struct tnode tnode;


tnode *newTree();
tnode *newNode();
tnode *addNode(tnode *, char *, int);
tnode *addNode_supplementare(tnode *, tnode *, char *, int, int);
void printTree(tnode *);
int contaNodi(tnode *);
int contaFoglie(tnode *);
int calcolaAltezza(tnode *);
char *search(tnode *, int);
boolean testNode(tnode *, int);
tnode *min(tnode *);
tnode *max(tnode *);
tnode *predecessore(tnode *);
tnode *successore(tnode *);


tnode *newTree(){   // Crea il root node dell'albero e lo inizializza a NULL
    return NULL;
}

tnode *newNode(){    // Crea nuovo nodo allocandone memoria 
    return malloc(sizeof(tnode));
}

int contaNodi(tnode *t){

    if(t != NULL) return 1 + contaNodi(t->left) + contaNodi(t->right);
    return 0;

}

int contaFoglie(tnode *t){

    if(t == NULL) return 0;
    if(t->left == NULL && t->right == NULL) return 1;
    return contaFoglie(t->left) + contaFoglie(t->right);

}

int calcolaAltezza(tnode *t){

    if(t == NULL) return -1;    // per convenzione l'albero vuoto ha altezza -1
    int sin = calcolaAltezza(t->left);
    int des = calcolaAltezza(t->right);
    if(sin >= des) return 1+sin;
    else return 1+des;

}

void printTree(tnode *t){
    
    if(t != NULL){
        printTree(t->left);
        printf("%d, ", t->key);   // visita del BST in ordine simmetrico
        printTree(t->right);
    }

}

char *search(tnode *t, int key){

    if(t != NULL){
        if(t->key == key) return t->element;
        else if(key < t->key) return search(t->left, key);
        else return search(t->right, key);
    }
    return NULL;

}

tnode *addNode(tnode *t, char *elem, int key){

    if(elem != NULL){
        int length = strlen(elem);
        return addNode_supplementare(t, NULL, elem, length, key);
    }
    else return t;

}

tnode *addNode_supplementare(tnode *t, tnode *parent, char *elem, int length, int key){

    if(t == NULL){
        t = newNode();
        t->element = malloc(sizeof(char)*(length+1));
        strcpy(t->element, elem);
        t->key = key;
        t->parent = parent;
        t->left = t->right = NULL;
    }
    else if(key < t->key){ t->left = addNode_supplementare(t->left, t, elem, length, key); }
    else if(key > t->key){ t->right = addNode_supplementare(t->right, t, elem, length, key); }
    return t;

}

boolean testNode(tnode *t, int key){  // restituisce true (= 1) se esiste nel bst un nodo con chiave "key" di input

    if(t != NULL){
        if(key == t->key) return true;
        else if(key < t->key) return testNode(t->left, key);
        else return testNode(t->right, key);
    }
    return false;

}

tnode *min(tnode *t){

    if(t != NULL){
        tnode *p = t;
        while(p->left != NULL) p = p->left;
        return p;
    }
    return NULL;

}

tnode *max(tnode *t){

    if(t != NULL){
        tnode *p = t;
        while(p->right != NULL) p = p->right;
        return p;
    }
    return NULL;

}

tnode *predecessore(tnode *t){  // il predecessore di un nodo v e' il nodo con chiave massima tra tutti i nodi con chiave <= chiave(v)

    if(t->left != NULL) return max(t->left);
    while(t->parent != NULL && t == t->parent->left) t = t->parent;
    return t->parent;

}

tnode *successore(tnode *t){  // il successore di un nodo v e' il nodo con chiave minima tra tutti i nodi con chiave >= chiave(v)

    if(t->right != NULL) return min(t->right);
    while(t->parent != NULL && t == t->parent->right) t = t->parent;
    return t->parent;

}

void main(){

    tnode *t = newTree();
    
    t = addNode(t, "prova", 10); t = addNode(t, "bst", 5); t = addNode(t, "programma", 28); t = addNode(t, "dati", 25);
    t = addNode(t, "algoritmi", 1); t = addNode(t, "strutture", 6); t = addNode(t, "dati", 30); t = addNode(t, "albero", 32);
    printTree(t); printf("\n");

    printf("L'albero ha %d nodi in totale\n", contaNodi(t));
    printf("L'albero ha %d foglie\n", contaFoglie(t));
    printf("L'albero ha altezza %d\n", calcolaAltezza(t));

}
