#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool squareIsWhite(char * coordinates){
    return (coordinates[0]-96+coordinates[1]-48) % 2 == 0 ? false : true;
}