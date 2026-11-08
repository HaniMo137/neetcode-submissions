class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]].append(i)
            else :
                dict[nums[i]] = [i]
        print(dict)
        for x in nums:
            y = target-x
            if y in dict :
                if y == x and len(dict[x]) > 1:
                    return [dict[x][0],dict[x][1]]
                elif y == x:
                    continue
                return [dict[x][0], dict[target-x][0]]