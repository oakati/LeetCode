class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int> myarray(0);
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == target){
                myarray.push_back(i);
            }
        }
        return myarray;
    }
};