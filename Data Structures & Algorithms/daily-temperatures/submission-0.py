class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        l = []
        res = [0] * len(t)
        for i in range(len(t)) :
            if len(l) == 0 :
                l.append(i)
            while t[i] > t[l[-1]]:
                c = l.pop()
                res[c] = i - c
                if len(l) == 0 : break
            l.append(i)
        return res
                
                