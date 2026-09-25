class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.prev = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = val if (self.min == None or val < self.min) else self.min
        self.prev.append(self.min)

    def pop(self) -> None:
        self.prev.pop()
        self.stack.pop()
        self.min = None if self.prev == [] else self.prev[-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prev[-1]