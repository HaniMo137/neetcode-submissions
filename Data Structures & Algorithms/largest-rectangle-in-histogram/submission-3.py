class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = []
        m = 0
        for i in heights :
            if len(l) == 0:
                l.append([i,1])
                continue
            c = 0
            while i < l[-1][0] :
                c += l[-1][1]
                m = max(m,l[-1][0]*c)
                l.pop()
                if len(l) == 0:
                    break
            if len(l) == 0:
                l.append([i,c+1])
                continue
            if l[-1][0] == i :
                l[-1][1] += 1+c
            else :
                l.append([i,c+1])
        c = 0
        while len(l) != 0:
            c += l[-1][1]
            m = max(m,l[-1][0]*c)
            l.pop()

        return m
            

            

               