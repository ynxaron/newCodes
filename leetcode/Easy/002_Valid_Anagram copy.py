# Using a hashmap to store the hashed version of left string and
# then going character to character to the right string to check
# whether or not it is in our left hashmap
def valid_anagrams(l: str, r: str) -> bool:
    l_set = set(l)
    for c in r:
        if c not in l_set:
            return False
    return True

print(valid_anagrams("hello", "eollh"))
