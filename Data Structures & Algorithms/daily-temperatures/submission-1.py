class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)) :
            if len(l) == 0 :
                l.append(i)
            while temperatures[i] > temperatures[l[-1]]:
                c = l.pop()
                res[c] = i - c
                if len(l) == 0 : break
            l.append(i)
        return res
                
                