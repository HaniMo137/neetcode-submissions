from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = deque([1])
        for i in range(len(nums)-1) :
            l.append(nums[i]*l[i])
            r.appendleft(nums[-i-1]*r[-i-1])
        r = list(r)
        return [x*y for x,y in zip(l,r)]