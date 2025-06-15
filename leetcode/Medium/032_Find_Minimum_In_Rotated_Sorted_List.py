# The answer is the same as 031, where we search for where the breaking inx is
# then simply returning the value there
def find_minimum_in_rotated_sorted_list(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[r]: # searching if the breaking inx is between m and r
            l = m + 1
        else:
            r = m - 1

    return nums[l]

print(find_minimum_in_rotated_sorted_list([3, 4, 5, 1, 2]))
