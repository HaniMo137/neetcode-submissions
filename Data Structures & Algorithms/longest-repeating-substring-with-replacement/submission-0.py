class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        i , j = 0, 0
        m = 1
        while j < len(s):
            if s[j] not in  map:
                map[s[j]] = 1
            else : 
                map[s[j]] += 1
            mm = 0
            for key in map :
                mm = max(mm, map[key])
            while (j-i+1) - mm > k :
                map[s[i]] -= 1
                i += 1
                mm = 0
                for key in map :
                    mm = max(mm, map[key])
            m = max(j-i+1,m)
            j += 1
        return m