#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool squareIsWhite(char * coordinates){
    return (coordinates[0]+coordinates[1]) % 2 != 0;
}