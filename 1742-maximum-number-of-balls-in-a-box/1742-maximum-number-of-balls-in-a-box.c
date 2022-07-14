#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 45
#define MAX(a,b) (((a)>(b))?(a):(b))

int countBalls(int lowLimit, int highLimit){
    int* array = malloc(SIZE*sizeof(int));
    char* text = malloc(7*sizeof(char));
    int sum, n, record = 0;
    for(int i = 0; i < SIZE; i++)
    {
        array[i] = 0;
    }
    for(int i = lowLimit; i <= highLimit; i++)
    {
        n = sprintf(text, "%d", i);
        sum = -48*n;
        do
        {
            sum += *text;
            text++;
        }while(*text);
        text -= n;
        array[sum-1]++;
        record = MAX(array[sum-1], record);
    }
    return record;
}