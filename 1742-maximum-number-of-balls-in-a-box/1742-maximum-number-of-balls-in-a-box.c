#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 45
int countBalls(int lowLimit, int highLimit){
    int* array = malloc(SIZE*sizeof(int));
    char text[7];
    int sum, n, record;
    for(int i = 0; i < SIZE; i++)
    {
        array[i] = 0;
    }
    record = 0;
    for(int i = lowLimit; i <= highLimit; i++)
    {
        sum = 0;
        n = sprintf(text, "%d", i);
        for(int j = 0; j < n; j++)
        {
            sum += text[j]-48;
        }
        array[sum-1]++;
        record = array[sum-1] > record ? array[sum-1] : record;
    }
    /*record = 0;
    for(int i = 0; i < SIZE; i++)
    {
        if(array[i] > record)
        {
            record = array[i];
        }
    }*/
    return record;
}