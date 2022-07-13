#include <stdio.h>
#include <stdlib.h>
int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize){
    int sum = 0, a, b, c;
    for(int i = 0; i < pointsSize-1; i++)
    {
        a = abs(points[i+1][1]-points[i][1]);
        b = abs(points[i+1][0]-points[i][0]);
        sum += (a > b ? a : b);
    }
    return sum;
}