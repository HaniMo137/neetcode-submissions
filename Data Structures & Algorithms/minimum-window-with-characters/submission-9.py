class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = {}
        dmap = {}
        if len(s) < len(t) :
            return ""
        if t == "" or s == "":
            return ""
        for i in t :
            if i in map:
                map[i] += 1
            else :
                map[i] = 1
                dmap[i] = 0
        ind = []
        for i in range(len(s)):
            if s[i] in map :
                ind.append(i)
        if len(ind) == 0:
            return ""
        j = 0
        dmap[s[ind[0]]] = 1
        c = len(map)
        if dmap[s[ind[0]]] >= map[s[ind[0]]] :
            c -= 1
        sat = 0
        st , end = 0 , 0
        for k in range(len(ind)):
            i = ind[k]
            while c != 0 and j < len(ind)-1 :
                j += 1
                dmap[s[ind[j]]] += 1
                if dmap[s[ind[j]]] == map[s[ind[j]]] :
                    c -= 1
            if  c == 0:
                if sat == 0:
                    st = i
                    end = ind[j]
                    sat = 1
                elif  end - st > ind[j] - i :
                    st = i
                    end = ind[j]
            else :
                break
            dmap[s[i]] -= 1
            if dmap[s[i]] < map[s[i]] :
                c += 1
        if sat == 0 : return ""
        return s[st:end+1]
             
        