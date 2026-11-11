class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = [(target-position[i])/speed[i] for i in range(len(position))]
        ind = sorted(range(len(position)), key = lambda i: position[i])
        l = []
        for i in ind:
            if len(l) == 0 :
                l.append(i)
                continue
            while t[i] >= t[l[-1]]:
                l.pop()
                if len(l) == 0: break
            l.append(i)
        return len(l)
