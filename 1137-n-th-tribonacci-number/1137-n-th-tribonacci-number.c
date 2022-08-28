

int tribonacci(int n){
    switch(n)
    {
        case 0:
            return 0;
            break;
        case 1:
            return 1;
            break;
        case 2:
            return 1;
            break;
    }
    int arr[n+1];
    for(int i = 0; i <= n; i++)
    {
        arr[i] = 0;
    }
    arr[1] = 1;
    arr[2] = 1;
    for(int i = 3; i <= n; i++)
    {
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3];
    }
    return arr[n];
}