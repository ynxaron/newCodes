# The core idea is to first iterate through all the elements,
# then find those elements which has nothing before it, no element
# smaller than it in the array, then increment till it finds a value
# that is a value that is not in the set. For example, for e if (e - 1) is not
# present, but (e, e + 1, e + 2 and e + 3) is present, but not (e + 4), then iterating
# it would increment the length till it finds j such that (e + j) is not present
def longest_consecutive_seq(inp: list[int]) -> int:
    max_len = 0
    inp_set = set(inp)

    for e in inp:
        if (e - 1) not in inp_set: # checking it is one of those core elements
            j = 0
            while (e + j) in inp_set: # iterating till (e + j) is not present
                j += 1
            max_len = max(max_len, j) # taking the max value of previous lengths and this one
    return max_len

print(longest_consecutive_seq([100, 4, 200, 1, 3, 2]))
