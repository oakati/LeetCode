#include <stdio.h>
#include <string.h>

void reconsPerm(char * s, int* myarray, int* returnSize)
{
    int a = 0, b = *returnSize-1;

    for(int i = 0; i < (*returnSize)-1; i++)
    {
        if(s[i] == 'I')
        {
            myarray[i] = a;
            a++;
        }
        else
        {
            myarray[i] = b;
            b--;
        }    
    }
    myarray[(*returnSize)-1] = b;
}

int* diStringMatch(char * s, int* returnSize){
    *returnSize = strlen(s)+1;
    int* myarray = malloc(*returnSize*sizeof(int));
    reconsPerm(s, myarray, returnSize);
    return myarray;
}