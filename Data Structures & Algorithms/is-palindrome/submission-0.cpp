class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        for (int j = 0; j < s.size(); j++){
            if (isalnum(s[j])){
                s[i] = tolower(s[j]);
                i++;
            }
        }
        s.resize(i);
        cout << s;
        for (int j = 0; j < i/2; j++){
            if (s[j] != s[i-j-1])
               return false;
        }
        return true;
    }
};
