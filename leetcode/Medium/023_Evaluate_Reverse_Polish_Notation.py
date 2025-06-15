# the crux of this algorithm is to use a stack that would append the element
# till we get a symbol, then we pop the stack twice to have first and second value
# then using these values to do the operation, and appending to the stack the result of
# that operation
def evaluate_reverse_polish_notation(inp: list[str]) -> int:
    evaluation_stack = [] # this would have all the elements which we would pop
    for c in inp:
        if c == "+":
            f = evaluation_stack.pop()
            # this because the first element that would be popped would be the later element
            s = evaluation_stack.pop()
            # while the second element to be popped would be the first element
            evaluation_stack.append(f + s)
        if c == "*":
            f = evaluation_stack.pop()
            s = evaluation_stack.pop()
            evaluation_stack.append(f * s)
        if c == "/":
            f = evaluation_stack.pop()
            s = evaluation_stack.pop()
            evaluation_stack.append(int(f / s))
        if c == "-":
            f = evaluation_stack.pop()
            s = evaluation_stack.pop()
            evaluation_stack.append(f - s)
        else:
            evaluation_stack.append(int(c))

    return evaluation_stack[-1]
