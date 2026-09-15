class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,vector<int>> id;
        for (int i = 0 ; i < nums.size() ; i++){
            id[nums[i]].push_back(i);
        }
        sort(nums.begin(),nums.end());
        int i = 0 ;
        int j = nums.size()-1;
        int x;
        while (i < j){
            x = target - nums[j];
            cout << x << i << j;
            if (x == nums[i])
                break;
            else if (x < nums[i])
                j--;
            else
                i++;
            cout << x << i << j;
        }
        if (nums[i] == nums[j])
            return {id[nums[i]][0],id[nums[j]][1]};
        if (id[nums[i]][0] < id[nums[j]][0])
            return {id[nums[i]][0],id[nums[j]][0]};
        return {id[nums[j]][0] , id[nums[i]][0]};
        }
};
