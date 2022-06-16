public class Solution {
    public bool CheckPerfectNumber(int num) {
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
            for(int i = 1; i < num; i++)
            {
                if(num % i == 0)
                {
                    count += i;
                }
            }
            return count == num;
        }

    }
}