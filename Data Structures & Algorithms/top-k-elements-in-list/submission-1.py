class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else :
                dict[i] = 1
        l = list(dict.keys())
        l.sort(key=lambda nb: -dict[nb])
        return l[:k]