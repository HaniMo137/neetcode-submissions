class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def tsum(target,nbs):
            i,j = 0,len(nbs)-1
            l = []
            while i < j :
                s = nbs[i] + nbs[j]
                if s == target: 
                    l.append([-target,nbs[i],nbs[j]])
                    i += 1
                    j -= 1
                    while i < j and nbs[i] == nbs[i-1] :
                        i += 1
                elif s < target: i += 1
                else : j -= 1
            return l
        nums.sort()
        res = []
        print(nums)
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            l = tsum(-nums[k],nums[k+1:])
            if len(l) != 0:
                res.extend(l)
        return res