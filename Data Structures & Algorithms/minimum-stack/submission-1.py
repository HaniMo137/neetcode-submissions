class MinStack:

    def __init__(self):
        self.l = []
        self.m = []
    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.m) == 0 :
            self.m.append(val)
        elif val <= self.m[-1]:
            self.m.append(val)

    def pop(self) -> None:
        x = self.l.pop()
        if x == self.m[-1]:
            self.m.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.m[-1]
