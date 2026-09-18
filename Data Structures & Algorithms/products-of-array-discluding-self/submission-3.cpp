class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector <int> pr(n, 1);
        vector <int> sf(n, 1);
        vector <int> arr(n, 1);
        for (int i = 1; i < n; i++)
            pr[i] = nums[i-1] * pr[i-1];
        for (int i = n-2; i >= 0; i--)
            sf[i] = nums[i+1] * sf[i+1];
        for (int i = 0; i < n; i++)
            arr[i] = pr[i]*sf[i];
        return arr;
    }
};
