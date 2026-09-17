class Solution {
public:

    string encode(vector<string>& strs) {
        string s = to_string(strs.size())+"@";
        for (string ss: strs){
            s += to_string(ss.size())+"@"+ss;
        }
        return s;
    }

    vector<string> decode(string s) {
        vector <string> strs;
        int i = 0;
        while (s[i] != '@')
            i++;
        int size = stoi(s.substr(0,i));
        i++;
        for (int k = 0; k < size; k++){
            int a = 0;
            while(s[i+a]!= '@')
                a++;
            int len = stoi(s.substr(i,a));
            i = i+a+1;
            strs.push_back(s.substr(i,len));
            i += len;
        }
        return strs;
    }
};
