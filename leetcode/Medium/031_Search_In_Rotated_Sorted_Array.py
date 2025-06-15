# The crux of this solution depends upon first finding where exactly is the
# break in between otherwise sorted list. We do it by checking the middle value
# is bigger than right value, that is somewhere between middle and right there is the
# break inx, otherwise somewhere between left and middle there is the breaking index
def search_in_rotated_sorted_arr(nums: list[int], target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[r]: # if the sorted list broke somewhere in middle of m and r
            l = m + 1
        else:
            r = m - 1

    # Then we create a function that takes normal variable and converts it in variabls
    # that takes the breaking index into consideration
    def inx(i: int) -> int:
        new_inx = l + i # since 0 is fist index, at breaking index is where it should begin
        while new_inx >= len(nums): # since, if this inx is bigger than length, just wrap around it
            new_inx -= len(nums)
        return new_inx

    # Then simply do the normal binary search, just convert the normal index to inx(index)
    e, w = 0, len(nums) - 1
    while e <= w:
        m = (e + w) // 2
        if nums[inx(m)] == target:
            return True
        if nums[inx(m)] < target:
            e = m + 1
        if nums[inx(m)] > target:
            w = m - 1
    return False

print(search_in_rotated_sorted_arr([4, 5, 6, 7, 0, 1, 2], 0))
print(search_in_rotated_sorted_arr([5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 0))
