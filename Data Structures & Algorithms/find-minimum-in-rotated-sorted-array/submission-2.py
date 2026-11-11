class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        i, j = 0, len(nums)-2
        while i <= j:
            if nums[i] < nums[i-1]:
                return nums[i]
            elif nums[j] > nums[j+1]:
                return nums[j+1]
            p = (i+j) // 2
            if nums[p] > nums[j]:
                i = p+1
            else :
                j = p-1
