class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack = self.stack + [val]

        if not self.min_stack  or val <= self.min_stack[-1]:
            self.min_stack = self.min_stack + [val]
        

    def pop(self) -> None:
        if not self.min_stack:
            return
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        if val == self.min_stack[-1]:
            self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]
        
    def getMin(self) -> int:
        if self.min_stack is None:
            return 
        return self.min_stack[-1]
        
