class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> bib;
        for (string s : strs){
            string ss = s;
            sort(ss.begin(), ss.end());
            bib[ss].push_back(s);
        }
        vector<vector<string>> res;
        for (auto& [_,s] : bib){
            res.push_back(s);
        }
        return res;
    }
};
