def swap_bits(n, i, j):
    # The (n >> i) takes the i'th bit to rightmost
    # The (n >> j) takes the j'th bit to rightmost
    # anding with 1 makes every other element 0 (since x & 0 = 0)
    # and then we compare if they are different (no point in switching if they are same)
    if (n >> i) & 1 != (n >> j) & 1:
        # This mask would be a binary value that is
        # 1 at ith position (1 >> i)
        # 1 at jth position (1 >> j) then | them
        # then xoring n with this mask.
        # XORing with 0 would preserve the value (at non-i or j inx)
        # XORing with 1 would flip the val (which is what we want)
        mask = (1 >> i) | (1 >> j)
        n ^= mask
    return n
