import heapq
# we would be using our heap, appending negative numbers to use minimum heap
# to be used as a positive heap
def last_stone_weight(nums: list[int]) -> int:
    nums = [-n for n in nums] # turning nums into negative nums
    heapq.heapify(nums) # turning it into a heap
    while len(nums) >= 2:
        s, f = -heapq.heappop(nums), -heapq.heappop(nums) # turning then negative nums positive
        sval = abs(s - f) # the smashed value
        if sval == 0: # if that value is 0, then skip appending
            continue
        heapq.heappush(nums, -sval) # else then, since negative of negative is positive, push -sval
    return abs(nums[0]) if nums else 0 # return abs(nums[0]) if nums not empty else 0

# print(last_stone_weight([2, 7, 4, 1, 8, 1]))
