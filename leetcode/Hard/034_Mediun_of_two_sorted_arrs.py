# The crux of this algorithm depends upon the realization that if we can
# find two indeces am and bm such that A[am] <= B[bm + 1] and B[bm] <= A[am + 1]
# then all the values between (1..max(A[m], B[m])) would be in between these two slices
# so, if we need to figure out the mediun, then we can have two substrings such that
# there length add up to half the total length and they fulfull the above stated property
def mediun_of_two_sorted_arrays(A: list[int], B: list[int]) -> float | None:
    if len(B) < len(A):
        A, B = B, A # always making sure array 'A' is the shorted one
    while True:
        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) // 2
            am = ((len(A) + len(B) + 1) // 2) - m - 2

            bleft = B[m] if m >= 0 else float("-infinity")
            bright = B[m + 1] if m < len(B) - 1 else float("infinity")
            aleft = A[am] if am >= 0 else float("-infinity")
            aright = A[am + 1] if am < len(A) - 1 else float("infinity")

            if aleft <= bright and aright <= bleft: # it fulfill the above stated condition
                if (len(A) + len(B) + 1) % 2 == 0: # if the length is even, then take the middle value
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) // 2 # else take the value in between

            if aleft > bright: # else, if aleft > bright, then we need to make aleft smaller
                r = m + 1
            if bleft > aright: # or, if bleft > aright, then we need to make aleft, hence aright bigger
                l = m - 1
    return None

print(mediun_of_two_sorted_arrays([1, 2], [3, 4]))
