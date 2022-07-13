#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int findSmallest(int* nums, int numsSize)
{
    int record = 1000;
    for(int i = 0; i < numsSize; i++)
    {
        record = MIN(record, nums[i]);
    }
    return record;
}

int findGreatest(int* nums, int numsSize)
{
    int record = 1;
    for(int i = 0; i < numsSize; i++)
    {
        record = MAX(record, nums[i]);
    }
    return record;
}

int findGCD(int* nums, int numsSize){
    int sn = findSmallest(nums, numsSize);
    int gn = findGreatest(nums, numsSize);
    
    for(int i = gn-sn; i > 0; i-- )
    {
        if(gn % i == 0 && sn % i == 0)
            return i;
    }
    return gn;
}