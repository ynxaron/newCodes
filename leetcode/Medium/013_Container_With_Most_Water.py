# The trick behind this algorithm is to realize that the area would be better if the
# distance between them is larger. Hence, if we begin with the largest area (l = 0, r = len(inp) - 1)
# We use it because we can make sure we are at all consideration optimizing one of the two factors that
# determine the area of the water, the length between them. We begin with the largest size, and decrement
# that which is smaller (so that we can potentially increse the lower bound)
def container_with_most_water(inp: list[int]) -> int:
    area = 0
    l, r = 0, len(inp) - 1
    while l < r:
        area = max(area, (r - l) * min(inp[l], inp[r]))
        if inp[l] < inp[r]: # so that the smaller element maybe potentially increased
            l += 1
        else:
            r -= 1
    return area

print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
