# The crux of this algorithm is to use the fact that, if for speed m our hours
# are valid, then it is valid for all speed above that, and since we are seeking the
# minimum speed, we must only search from l-->(m - 1) (since 'm' has also been searched)
# and if not, if 'm' is not valid, then we must search from (m + 1)-->r
import math
def koko_eating_banana(piles: list[int], hours: int) -> int:
    l, r = 1, max(piles) # 1 and not 0 because it does not make sense to have 0 speed
    min_speed = r
    while l <= r:
        m = (l + r) // 2
        this_hour = 0
        for p in piles: # calculating the total time
            this_hour += math.ceil(p / m)
        if this_hour <= hours: # if this_hour is valid
            min_speed = min(min_speed, this_hour)
            r = m - 1 # searching from (m - 1)
        else:
            l = m + 1

    return min_speed

print(koko_eating_banana([3, 6, 7, 11], 8))
