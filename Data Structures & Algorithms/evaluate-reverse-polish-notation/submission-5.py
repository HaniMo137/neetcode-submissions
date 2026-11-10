class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        for c in tokens :
            if c not in ['+','-','*','/' ]:
                l.append(int(c))
            else :
                b = l.pop()
                a = l.pop()
                if c == '+' :
                    l.append(a+b)
                elif c == '-' :
                    l.append(a-b)
                elif c == '*' :
                    l.append(a*b)
                elif c == '/' :
                    l.append(int(a/b))
        return l[0]