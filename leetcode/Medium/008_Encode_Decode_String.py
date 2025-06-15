def encode_decode():
    # We would be encoding in a single such that we would have a number
    # indicating the length of the word, followed by a "#", followed by
    # other words, putting it all in a single list
    def encode(inp: list[str]) -> str:
        r = ""
        for s in inp:
            r += str(len(s)) + "#" + s
        return r

    def decode(s: str) -> list[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": # decoding till we found a "#" symbol
                j += 1
            length = int(s[i:j]) # since s[j] is the "#", s[i:j] would be where the length variable resides
            words.append(s[j+1:j+length+1]) # since at (j + 1) is the first letter, (j + 2) second letter
                            # and (j + n) the nth letter, we would slice from (j + 1) to (j + n + 1)
            i = j + length + 1
        return words

    return (encode, decode)

enc, dec = encode_decode()
ans = enc(["lint", "code", "love", "you"])
print(ans)
ques = dec(ans)
print(ques)
