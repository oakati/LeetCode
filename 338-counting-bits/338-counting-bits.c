

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize){
    *returnSize = n + 1;
    int* ans = malloc((n+1)*sizeof(int));
    int counter, kalan, bolum;
    *(ans) = 0;
        for(int i = 1; i <= n ; i++){
            counter = 1;
            bolum = i;
            while(bolum != 1){
                kalan = bolum % 2;
                bolum = bolum / 2;
                if(kalan == 1)
                    counter++;
            }
            *(ans+i) = counter;
        }
    return ans;
}