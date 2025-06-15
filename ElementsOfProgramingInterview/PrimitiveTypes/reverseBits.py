LOOKUP = {}
# The logic of this algorithm is to use the cached table again, but this time
# for the reversal of each 16-bit value, then dragging the least 16-bit value to
# the most 16-bit value (the << (3 * MASK_SIZE)), then taking the second last
# 16-bit value, dragging it, reversing it, then dragging it left to twice the MASK_SIZE
def reverse_bits(n):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF; # will make ever other bit apart from last 16 one 0
    final_digit  = LOOKUP[n & BIT_MASK] << (3 * MASK_SIZE)
    final_digit |= LOOKUP[(n >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE)
    final_digit |= LOOKUP[(n >> 2 * MASK_SIZE) & BIT_MASK] << MASK_SIZE
    final_digit |= LOOKUP[(n >> 3 * MASK_SIZE) & BIT_MASK]
    return final_digit
