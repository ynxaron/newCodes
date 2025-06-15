from collections import defaultdict
# Using a list of size 26 to fingerprint any word such that any other word
# that might be an anagram is captured as same, then using that fingerpting as
# an index to append two words that are anagrams into a single list
def group_anagrams(inp: list[str]) -> list[list[str]]:
    anagram_group = defaultdict(list)
    for s in inp:
        alphabet_fingerprint = [0] * 26
        for c in s:
            alphabet_fingerprint[ord(c) - ord('a')] += 1
        anagram_group[tuple(alphabet_fingerprint)].append(s)
    return list(anagram_group.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
