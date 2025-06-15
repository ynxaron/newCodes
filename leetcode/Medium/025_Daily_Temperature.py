# The crux of this soln is to use a stack with both temp and inx
def daily_temperature(inp: list[int]) -> list[int]:
    stack = []
    res = [0] * len(inp)
    for i, t in enumerate(inp):
        while stack and t > stack[-1][0]:
            stack_t, stack_i = stack.pop()
            # appending at the index of where it is getting popped
            # between that index and the index whose element is bigger
            res[stack_i] = (i - stack_i)
        stack.append((t, i))
    return res

# print(daily_temperature([7, 6, 2, 4, 8, 6, 7]))
# print(daily_temperature([73, 74, 75, 71, 69, 72, 76, 73]))
# print(daily_temperature([30, 40, 50, 60]))
# print(daily_temperature([30, 60, 90]))
