import heapq
# using min-heap, with negative of the numbers (hence using it as a max-heap)
# and then popping and replacing values till k hit 0, and you have your
# kth largest value
def kth_largest_element_in_an_array(nums: list[int], k: int) -> int:
    nums = [-n for n in nums] # negating all values
    heapq.heapify(nums)
    res = -heapq.heappop(nums) # popping largest value, since otherwise I have to initialize it as None
    while k > 1: # since one has already been popped, we would decrement k till it hit 1
        res = -heapq.heappop(nums) # replacing res
        k -= 1
    return res

# print(kth_largest_element_in_an_array([3, 2, 1, 5, 6, 4], 2))
# print(kth_largest_element_in_an_array([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
