# Using the seen hashmap to store each value that we encounter,
# but before that checking if we were to subtract this value at present
# with target, would that value then would be available in the hashmap
def two_sum(inp: list[int], target: int) -> list[int]:
    seen = {}
    for e in inp:
        if (target - e) in seen:
            return [e, target - e]
        seen[e] = True
    return []

print(two_sum([3, 5, 4, 1, 5], 6))
