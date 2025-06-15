from collections import deque # we would be using a monotic decreasing queue
def sliding_window_maximum(inp: list[int], k: int) -> list[int]:
    res = []
    q = deque()
    l, r = 0, 0
    while r < len(inp):
        while q and inp[q[-1]] < inp[r]: # making sure it is always non-increasing
            q.pop()
        q.append(r)

        if l > q[0]: # if it come to that our left inx is out of bound
                     # that is we cannot take the leftmost, biggest element
                     # then we must take that index out, pop from left
            q.popleft()

        if (r + 1) >= k: # if our window is big enough, we take the biggest element
            res.append(inp[q[0]])
            l += 1       # and we increase our left pointer, to make sure it left pointer
                         # is smaller than or equal to biggest element
        r += 1
    return res

print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
