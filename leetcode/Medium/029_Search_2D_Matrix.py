# The idea behind this algorithm is to know the only plausible arrays
# where our target can be is where the first element is either smaller than
# or equal to the target. We append all those indeces in a special array, then
# iteratively perform binary search over them to figure out whether it has the element
def search_2d_matrix(inp: list[list[int]], t: int) -> int:
    i = 0
    plausable_inxs = []
    while i < len(inp):
        if inp[i][0] <= t:   # that if, in the course of the array can we find the target.
                             # since if first element > t, all other elems would be as well
            plausable_inxs.append(i)
        i += 1
    for i in plausable_inxs: # iterating over each such arrays
        arr = inp[i]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == t:
                return True
            if arr[m] < t:
                l = m
            if arr[m] > t:
                r = m
    return False
