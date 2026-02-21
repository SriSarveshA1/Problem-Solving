class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[len(self.min_stack)-1]>= val:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        poped_ele = self.stack.pop(len(self.stack)-1)
        
        if self.min_stack[len(self.min_stack)-1] == poped_ele:
            self.min_stack.pop(len(self.min_stack)-1)

    def top(self) -> int:
        
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()