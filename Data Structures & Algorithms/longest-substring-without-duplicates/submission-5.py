class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        m = 0
        map = {}
        ind = 0
        for i in range(len(s)):
            if s[i] not in map :
                map[s[i]] = i+1
            elif map[s[i]] > ind :
                ind = map[s[i]] 
                map[s[i]] = i + 1
            else : 
                map[s[i]] = i + 1
            l = i - ind + 1
            m = max(l, m)
            

        return m