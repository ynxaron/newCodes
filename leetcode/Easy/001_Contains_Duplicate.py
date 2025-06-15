# We shall be using a dictionary to store and efficiently check whether or not
# we have seen the element in consideration before
def contains_duplicate(inp: list[int]) -> bool:
    seen = {}
    for e in inp:
        if e in seen: # If we found the element return False
            return False
        seen[e] = True
    return True # If we were throughout the running of the loop unable to find it, return True

print(contains_duplicate([5, 3, 1, 6, 4, 3]))
