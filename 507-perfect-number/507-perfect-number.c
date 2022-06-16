#include <math.h>

bool checkPerfectNumber(int num){
        int count = 0;
        if(num % 2 == 1)
        {
            return false;
        }
        else if(num == 1)
        {
            return true;
        }
        else
        {
            for(int i = 1; i < num/2+1; i++)
            {
                if(num % i == 0)
                {
                    count += i;
                    
                }

            }
            return count == num;
        }
}