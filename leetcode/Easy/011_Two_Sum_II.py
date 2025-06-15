# The key to this solution is, since our list is already sorted, to take advantage of that
# We would begin by having two pointers, i and j, pointed at 0 and len(inp) - 1 respectifully
# Then, we would take the sum of inp[i] and inp[j]. If this sum is smaller than target,
# then the only way to increase this sum is to increment the i
# if it is larger than we would decrement j, and if it equal then we got out sum
def two_sum_II(inp: list[int], target: int) -> list[int]:
    i, j = 0, len(inp) - 1
    while i < j:
        this_sum = inp[i] + inp[j]
        if this_sum < target: # this mean we would need a number greater than inp[i]. Since all
        # j bigger than or equal to has already been tested (that's the only way j has been decrepted')
        # we must increment i instead.
            i += 1
        if this_sum > target: # the same explanation as before
            j -= 1
        if this_sum == target:
            return [inp[i], inp[j]]

    return []

print(two_sum_II([2, 7, 11, 15], 9))
