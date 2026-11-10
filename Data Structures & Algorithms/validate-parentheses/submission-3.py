class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s :
            if len(l) == 0 :
                if c in ['}',')',']'] :
                    return False
                l.append(c)
            elif (c == ')' and l[-1] == '(') or (c == '}' and l[-1] == '{') or (c == ']' and l[-1] == '['):
                l.pop()
            elif c in ['}',')',']'] :
                return False
            else :
                l.append(c)
        if len(l) == 0:
            return True
        return False