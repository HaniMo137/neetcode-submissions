class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        sort(nums.begin(), nums.end());
        int max = 1, len = 1;
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] - nums[i-1] == 1){
                len++;
                continue;
            }
            if (nums[i-1] == nums[i])
            continue;
            if (max < len)
            max = len;
            len = 1;
        }
        if (max < len)
            max = len;
        len = 1;
        return max;
    }
};
