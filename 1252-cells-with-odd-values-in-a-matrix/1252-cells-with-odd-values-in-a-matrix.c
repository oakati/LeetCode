
int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize){
    int counter = 0, myarray[m][n];
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            myarray[i][j] = 0;
        }
    }  
    for(int i = 0; i < indicesSize; i++)
    {
        for(int j = 0; j < n; j++)
        {
            myarray[indices[i][0]][j] = 1 - myarray[indices[i][0]][j];
        }
        for(int j = 0; j < m; j++)
        {
            myarray[j][indices[i][1]] = 1 - myarray[j][indices[i][1]];
        }
        
    }
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            counter += myarray[i][j];
        }
    }
    return counter;
}