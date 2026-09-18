class Solution {
public:
    bool isValid(string s) {
        stack <int> hh;
        for (char x : s){
            if (hh.empty()){
                hh.push(x);
                continue;
            }
            if ((hh.top() == '(' && x == ')')||(hh.top() == '{' && x == '}')||(hh.top() == '[' && x == ']')){
                hh.pop();
                continue;
            }
            hh.push(x);
        }
        if (hh.empty())
            return true;
        return false;
    }
};
