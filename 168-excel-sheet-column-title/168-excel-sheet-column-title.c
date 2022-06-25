

char * convertToTitle(int columnNumber){
    char * ptr;
    ptr = malloc(8 * sizeof(char));
    ptr += 7;
    *ptr = 0;

    while(columnNumber)
    {
        ptr--;
        columnNumber = columnNumber - 1;
        *ptr = (columnNumber%26) + 65;
        columnNumber = columnNumber/26;
    }    

    return ptr;
}