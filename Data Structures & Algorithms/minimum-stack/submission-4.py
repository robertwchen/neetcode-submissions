class MinStack:
    stack = []
    min_stack = []



    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if smaller than top of min_stack then push to that
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        return
        

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        #print(self.stack, self.min_stack)
        return self.min_stack[-1]

        
