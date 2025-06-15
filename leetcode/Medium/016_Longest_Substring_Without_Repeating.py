# The crux of this algorithm depends upon the motion of sliding right till
# all numbers are unique, then creeping left pointer till we are unique again (or l == r)
def longest_substring_without_repeating(s: str) -> str:
    max_len = 0
    max_str = ""
    alphabet_window = [0] * 26 # alphabet tracking index
    l, r = 0, 0
    while r < len(s):
        alp_inx = ord('a') - ord(s[r])
        if alphabet_window[alp_inx] == 1: # if it is already 1, that is we already have seen the elem
            #print("The character " + "'" + s[r] + "'" + " has been found in " + "'" + s[l:r+1] + "'")
            #this_char = s[r]
            while s[l] != s[r] and l < r: # then, iterate till we have found the element that we have found earlier
                # if the first elem was the elem that was repeated, then this loop won't be entered
                # then keep repeating till we have found the repeating element
                l_inx = ord('a') - ord(s[l])
                alphabet_window[l_inx] = 0
                l += 1
            alphabet_window[ord('a') - ord(s[l])] = 0
            l += 1
            #print("Now, the character " + "'" + this_char + "'" + " is not in " + "'" + s[l:r+1] + "'\n\n")
        else: # else, if so far no element has been repeated
            alphabet_window[alp_inx] = 1 # then mark this new element is 'has found'
            if (r - l + 1) > max_len: # if this substring is the biggest
                max_len = l - r + 1 # simply change the largest string value
                max_str = s[l:r]
        r += 1

    return max_str

print(longest_substring_without_repeating("abcabcbb"))
