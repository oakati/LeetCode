

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize){
    *returnSize = n;
    int *myarray = malloc(n * sizeof(int));
    for(int i = -n/2; i <= n/2; i++)
    {
        if(n % 2 == 0 && i == 0)
        {
            continue;
        }
        else
        {
            *myarray = i;
            myarray++;
        }
    }
    myarray -= n;
    return myarray;
}