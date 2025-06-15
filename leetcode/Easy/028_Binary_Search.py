# The idea behind binary search is to exploit the fact that the list
# is sorted, and reorient our list by the middle value. If that middle
# value is greater than our target, then no value that would come after could
# be equal to our target either, and vica versa
def binary_search(inp: list[int], t: int) -> int | None:
    l, r = 0, len(inp) - 1
    while l <= r:
        m = (l + r) // 2
        if inp[m] == t: # if it is equal, we found our value
            return m
        if inp[m] < t: # else make the left pointer the middle one, discarding the right half
            l = m
        if inp[m] > t: # or discard the left half instead
            r = m
    return None

print(binary_search([-1, 0, 3, 5, 9, 12], 9))
