class MinStack:
    # Initializing our two stacks, min_stacks
    def __init__(self):
        self.stack     = []
        self.min_stack = []

    # Pushing on our stack
    def push(self, val: int):
        self.stack.append(val)
        if self.min_stack != []: # if our min_stack is not empty
            self.min_stack.append(min(self.min_stack[-1], val))
            # appending the minimum of the current value at top of stack, or the value we have
        else:
            # else we simply just append the value at the minimum
            self.min_stack.append(val)

    # returning the top element of our stack
    def top(self) -> int:
        return self.stack[-1]

    # popping the top of stack, as well as our minimum_stack
    def pop(self):
        self.min_stack.pop()
        self.stack.pop()

    # getting the minimum is as simple as getting the top of min_stack
    def getMin(self) -> int:
        return self.min_stack[-1]

def min_stack(ins: list[str], val: list[list[int]]) -> list[int | None]:
    if len(ins) != len(val): # if the instructions and value list are not equal, stop immediately
        return []
    minstack = None # minstack is None because it could be that we have 'push'
                    # before minstack is initialized
    res = []
    for i in range(len(ins)):
        ans = None
        if ins[i] == "MinStack":
            minstack = MinStack()
        if ins[i] == "push":
            if minstack is not None: # if we have a minstack
                minstack.push(val[i][0])
        if ins[i] == "pop":
            if minstack is not None: # if we have a minstack
                ans = minstack.pop()
        if ins[i] == "top":
            if minstack is not None: # if we have a minstack
                ans = minstack.top()
        if ins[i] == "getMin":
            if minstack is not None: # if we have a minstack
                ans = minstack.getMin()

        res.append(ans) 
    return res

print(min_stack(["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []]))
