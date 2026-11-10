class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ind = 0
        l = [0]
        res = []
        for i in range(1,k):
            while nums[l[-1]] <= nums[i] :
                l.pop()
                if len(l) == 0: break
            l.append(i)
        
        res.append(nums[l[ind]])
        for i in range(k,len(nums)):
            while nums[l[-1]] <= nums[i] :
                l.pop()
                if len(l) == 0: break
            l.append(i)
            if ind >= len(l) :
                ind = len(l) -1
            else :
                while l[ind] < i-k+1:
                    ind += 1
            res.append(nums[l[ind]])
        return res
            
        
            

        