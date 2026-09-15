class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> bib;
        
        for (int n : nums)
            bib[n]++;
        vector<pair<int, int>> res(bib.begin(), bib.end());
        sort(res.begin(),res.end(), [](auto& a, auto& b){
            return a.second > b.second;
        });
        vector <int> sol;
        
        for (int i = 0; i< k; i++){
            sol.push_back(res[i].first);
        }
        return sol;
    }
};
