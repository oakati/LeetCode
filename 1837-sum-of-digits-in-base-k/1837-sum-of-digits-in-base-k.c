int sumBase(int n, int k){
    int sum = 0;
    do
    {
        sum += n%k;
        n /= k; 
    }while(n != 0);
    return sum;
}