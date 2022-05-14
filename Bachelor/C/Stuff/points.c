#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define FLOAT_CONST 1.44  // ---> aumentala per concentrare di piu' i punti, diminuiscila per renderli piu' sparsi

struct point{

    float x, y;
    char label[16];

}; typedef struct point point;

void allocate(point *, int);

point getMaximumXPoint(point *, int);
point getMinimumXPoint(point *, int);

point getMaximumYPoint(point *, int);
point getMinimumYPoint(point *, int);

point getMinimumXPoint(point *points, int n){

    point min = points[0];

    for(int i = 1; i < n; i++){
        if(min.x > points[i].x) min = points[i];
    }
    
    return min;

}


point getMaximumXPoint(point *points, int n){

    point max = points[0];

    for(int i = 1; i < n; i++){
        if(max.x < points[i].x) max = points[i];
    }

    return max;

}

point getMinimumYPoint(point *points, int n){

    point min = points[0];

    for(int i = 1; i < n; i++){
        if(min.y > points[i].y) min = points[i];
    }

    return min;

}


point getMaximumYPoint(point *points, int n){

    point max = points[0];

    for(int i = 1; i < n; i++){
        if(max.y < points[i].y) max = points[i];
    }

    return max;

}

void allocate(point *points, int n){


    for(int i = 0; i < n; i++){
        points[i].x = (float)(rand()%1001)/(FLOAT_CONST);
        points[i].y = (float)(rand()%1001)/(FLOAT_CONST);
    }

}

int main(){

    srand(time(NULL));
    int n = rand()%1000+1;

    point *points = malloc(sizeof(point)*n);

    allocate(points, n);

    for(int i = 0; i < n; i++){
        printf("point number %d: %.2f, %.2f\n", i, points[i].x, points[i].y);
    }

    point minX = getMinimumXPoint(points, n);
    point maxX = getMaximumXPoint(points, n);

    printf("\nMinimum x point: %.2f, %.2f\nMaximum x point: %.2f, %.2f\n", minX.x, minX.y, maxX.x, maxX.y);

    free(points);
    return 1;

}