class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
            return False
        map = {}
        dmap = {}
        for i in s1 :
            if i in map :
                map[i] += 1
            else :
                map[i] = 1
                dmap[i] = 0
        i, j = 0, len(s1)-1
        for k in range(i,j+1):
            if s2[k] in dmap :
                dmap[s2[k]] += 1
        if map == dmap :
            return True
        while j < len(s2)-1:
            j += 1
            if s2[j] in dmap:
                dmap[s2[j]] += 1
            if s2[i] in dmap:
                dmap[s2[i]] -= 1
            i += 1
            if map == dmap :
                return True
        return False