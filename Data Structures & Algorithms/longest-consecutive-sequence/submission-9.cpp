class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        set<int> s;
        for (int x : nums)
        s.insert(x);
        int max = 0;
        int len = 0;
        int prev = 0;
        for (int x : s ){
            if (x - prev == 1){
                len += 1;
                prev = x;
                continue;
            }
            if (max < len)
            max = len;
            len = 1;
            prev = x;
        }
        if (max < len)
            max = len;
        return max;
    }
};
