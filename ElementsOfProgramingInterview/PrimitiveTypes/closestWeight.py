# Let us define 'weight' of a non-negative integers
# as the number of 1s in it's binary representation.
# Write a program that takes an input x and returns
# a number not equal to x that has the same weight
# as x and |y - x| is minimized.
#
# ANSWER ----------------------------------------------
# Our answer is based on figuring out from the right most
# significant bits pair (adjacent bits) moving to left
# and when finding a pair that differ, switching it up

def closest_weight(n: int) -> int:
    MAX_DIGIT_RANGE = 64
    for i in range(MAX_DIGIT_RANGE):
        # The ((n >> i) & 1) would make a bit at i'th (from right)
        # the only bit that remains same (making every other bit 0)
        if ((n >> i) & 1) != ((n >> (i + 1)) & 1):
            # The MASKING_BIT is a bit that is 1 and ith and (i + 1)th value
            # and apart from that is 0. When you XOR this bit with n, then
            # (0 xor 1 = 1 and 0 xor 0 = 0), making normal n that is not
            # in i'th or (i + 1)'th position same, but (1 xor 1 = 0 and 0 xor 1 = 1)
            # flipping the bits. Hence achieving our objective
            MASKING_BIT = (1 << i) | (1 << (i + 1))
            n ^= MASKING_BIT
            return n
    # if we unable to find a bit pair differing in value while searching all is
    # we raise a custom ValueError (since it is not suppose to happen)
    raise ValueError("All Bits are Either 1 or 0")
