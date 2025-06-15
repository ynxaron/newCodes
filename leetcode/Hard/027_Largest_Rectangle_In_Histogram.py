def largest_rectangle_histogram(inp: list[int]) -> int | None:
    max_area = None
    l, r = 0, len(inp) - 1
    while l < r:
        this_area = (r - l + 1) * min(inp[l], inp[r])
        print("Left   ==> '" + str(l) + "'")
        print("Right  ==> '" + str(r) + "'")
        print("Result ==> '" + str(this_area) + "'")
        print("\n\n")
        max_area = max(max_area, this_area) if max_area is not None else this_area
        if inp[l] < inp[r]:
            l += 1
        else:
            r -= 1
    return max(max_area, inp[r]) if max_area is not None else None

print(largest_rectangle_histogram([2, 1, 5, 6, 2, 3]))
