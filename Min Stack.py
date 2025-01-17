class MinStack:
    def __init__(self):
        self.stack = []
        self.tops = [None]

    def push(self, val: int) -> None:
        self.tops.insert(0, val)
        if len(self.stack) == 0:
            self.min = val
            self.stack.insert(0, val)
        else:
            if val >= self.min:
                self.stack.insert(0, val)
            else:
                self.stack.insert(0, (2 * val) - self.min)
                self.min = val

    def pop(self) -> None:
        self.tops = self.tops[1:]

        if self.stack[0] >= self.min:
            self.stack = self.stack[1:]
        else:
            self.min = (2 * self.min) - self.stack[0]
            self.stack = self.stack[1:]

    def top(self) -> int:
        return self.tops[0]

    def getMin(self) -> int:
        return self.min
    