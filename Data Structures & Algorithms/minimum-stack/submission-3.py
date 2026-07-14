class MinStack:

    def __init__(self):
        self.stack = []
        self.minSoFar = float('inf')

    def push(self, val: int) -> None:
        self.minSoFar = min(val, self.minSoFar)
        self.stack.append([val, self.minSoFar])

    def pop(self) -> None:
        value, minimum = self.stack.pop()
        if self.stack: 
            self.minSoFar = self.stack[-1][1]
        else:
            self.minSoFar = float('inf')
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
