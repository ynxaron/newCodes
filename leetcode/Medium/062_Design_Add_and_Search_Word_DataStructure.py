# The crux of this algorithm is to use a TrieNode, a simple Trie
# class methods except with added functionality of '.' char
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # this helper function is a recursive function that checks, whence
        # the word string is empty, whether that particular TrieNode is .endOfWord
        # Otherwise it would check whether the first character of the word is '.' or not.
        def helper(trie: TrieNode, word: str):
            if len(word) == 0:
                return trie.endOfWord
            chr = word[0]
            if chr == ".": # if yes
                for tries in trie.children.values(): # then check for all tries in this trie children
                    if helper(tries, word[1:]): # and if any of them return True
                        return True # return True ourselves
                return False # otherwise return False

            if chr in trie.children: # if chr is not ".", then we simply check if it is in trie.children
                return helper(trie.children[chr], word[1:]) # if yes, then we call recursive function one level down
            return False # else return False

        return helper(self.root, word) # call the helper function at the beginning of word with root node

#wordict = WordDictionary()
#wordict.addWord("bad")
#wordict.addWord("dad")
#wordict.addWord("mad")

#print(wordict.search("pad"))
#print(wordict.search("bad"))
#print(wordict.search(".ad"))
#print(wordict.search("b.."))
