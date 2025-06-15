# The crux of this algorithm depends upon using a two pointer technique
# to find the maxium (length wise) of the substring that is, as defined
# by a function within a function, valid. Here, valid means the length
# of the string - the length of the most occuring character is smaller than
# or equal to 'k', the characters we can replace. It is because we want to take
# those substrings which we can convert completely to a string that is made up
# entirely of a single character (by replacing all those characters that are not
# most occuring character)
def longest_repeating_character_replacement(inp: str, k: int) -> int:
    max_len = 0 # keeping track of the max_value
    def is_valid(s: str) -> bool:
        alphabet_inx = [0] * 26
        max_value = 0
        for c in s: # keeping track of most occuring element
            inx = ord(c) - ord('A')
            alphabet_inx[inx] += 1
            max_value = max(max_value, alphabet_inx[inx])
        return (len(s) - max_value) <= k # checking whether we can replace all other characters

    l, r = 0, 1
    while r < len(inp):
        if not is_valid(inp[l:r]): # if it is not valid, then increment 'l'
            l += 1
            continue # and try again
        #print("The left index is " + str(l) + " and the right index is " + str(r))
        #print("And the slice is: '" + inp[l:r] + "' The length is " + str(r - l) + "\n\n")
        max_len = max(max_len, r - l) # the only time this code would run is if inp[l:r] is valid
        r += 1
    return max_len

print(longest_repeating_character_replacement("AABABBA", 1))
