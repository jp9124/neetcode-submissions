class MinStack:

    def __init__(self):
        self.regular_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.regular_stack.append(val)
        if len(self.min_stack) > 0 and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])    
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.regular_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.regular_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
