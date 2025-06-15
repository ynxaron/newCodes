import heapq
# The crux of this algorithm is to use a heap, with the idea that .heapify function
# takes into consideration, when the values are list, only the first value when it is
# comparing values. We can make this value the distance (calculated with pythogerus formula)
# hence, it would be sorted with the value with lowest dist, and so on
def k_closest_points_to_origin(points: list[list[int]], k: int) -> list[list[int]]:
    dist_nums = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2) # calculating the distance
        dist_nums.append([dist, x, y]) # appending as the first value

    heapq.heapify(dist_nums)
    res = []
    while k > 0:
        _, x, y = heapq.heappop(dist_nums) # popping with least distance
        res.append([x, y]) # appending the points
        k -= 1 # reducing k, hence whence k is 0, res would have k points (sorted with least distance)

    return res

# print(k_closest_points_to_origin([[1, 3], [-2, 2]], 1))
