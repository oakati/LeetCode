#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int findNoOfDigits(int num)
{
    int len = 0;
    do
    {
        num /= 10;
        len++;
    }while(num != 0);
    return len;
}

int maximum69Number (int num){
    int len = findNoOfDigits(num);
    char mystr[10000];
    len = sprintf(mystr, "%d", num);  
    for(int i = 0; i < len; i++)
    {
        if(mystr[i] == '6')
        {
            mystr[i] = '9';
            break;
        }
    }
    return atoi(mystr);
}