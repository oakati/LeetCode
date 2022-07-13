

int sumOddLengthSubarrays(int* arr, int arrSize){
    int sum = 0;
    for(int i = 0; i < arrSize; i++)
    {
        for(int j = 1; j <= arrSize - i; j = j + 2)
        {
            for(int k = i; k < i+j; k++)
            {
                sum += arr[k];
            }
        }
    }
    return sum;
}