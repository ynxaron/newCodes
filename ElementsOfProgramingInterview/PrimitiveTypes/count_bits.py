# In this algorithm we are using 'n & 1' to see
# if the least significant bit is 1 or not. If 1, then
# 1 & 1 would be one, and bit_count would increase by 1
# else it would be zero. Then we just increment our bit
# represent right-word, adding 0 to most significant bit
def count_bits(n: int):
    bits_count = 0
    while n:
        bits_count += n & 1
        n >>= 1
    return bits_count
