class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        w = 0
        m = 0
        while i < j:
            l =  min(height[i],height[j])
            m = max(m,l)
            w += m-l
            if height[i] <= height[j]: i+=1
            else : j -=1
        return w