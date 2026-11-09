class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = prices[0]
        fp = 0
        p = 0
        for i in prices :
            p = max(p+i-k,0)
            fp = max(fp,p)
            k = i
        return fp