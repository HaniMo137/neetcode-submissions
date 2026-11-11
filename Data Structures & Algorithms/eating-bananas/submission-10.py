class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        def hours(p):
            hh = 0
            for i in piles:
                hh += math.ceil(i/p)
            return hh
        i, j = 1, m
        while i<j:
            p = (i+j)//2
            print(i,j)
            
            if hours(p) <= h:
                j = p
            else:
                i = p+1
        print(i,j)
        return i
            