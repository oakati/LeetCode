

int numberOfMatches(int n){
    int sum = 0, rem = 0;
    do
    {
        rem = n % 2;
        n /= 2;
        sum += n;
        n += rem;
    }while(n != 1);
    return sum;
}