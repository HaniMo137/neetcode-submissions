class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for x in strs : 
            sx = "".join(sorted(x))
            if sx in dict :
                dict[sx].append(x)
            else : 
                dict[sx] = [x]
        res = []
        for k in dict:
            res.append(dict[k])
        return res
        