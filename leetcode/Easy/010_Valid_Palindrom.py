# We would check character by character if, first, are they alphanumeral
# that is are they in between 'A' to 'Z' or 'a' to 'z' or '1' to '9'. If not
# then we simply skip them
# then we check whether they are similar to each other
def valid_palindrom(inp: str) -> bool:
    def is_alphanumeral(c: str) -> bool:
       is_capital = ord('A') <= ord(c) <= ord('Z')
       is_small = ord('a') <= ord(c) <= ord('z')
       is_number = ord('1') <= ord(c) <= ord('9')

       return is_capital or is_small or is_number

    i, j = 0, len(inp) - 1
    while i < j:
        if not is_alphanumeral(inp[i]): # we could have used a while loop as well, without a continue
            i += 1
            continue
        if not is_alphanumeral(inp[j]):
            j -= 1
            continue

        # making sure both inp[i] and inp[j] are alphanumerals before procedding
        if inp[i].lower() != inp[j].lower():
            print("'" + inp[i] + "'" + "is not equal to " + "'" + inp[j] + "'")
            return False
        else:
            i += 1
            j -= 1

    return True

print(valid_palindrom("A man, a plan, a canal: Panama"))
