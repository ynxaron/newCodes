class TrieNode:
    # the val of the (key, val) pair in the Trie Data Structure
    def __init__(self):
        self.children = {} # storing all children characters from current node
        self.endOfWord = False # determing whether this is end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children: # if the character in question is not in curr.children dict
                curr.children[c] = TrieNode() # then create a trie node at key 'c'
            curr = curr.children[c] # move to that value
        curr.endOfWord = True # at the end of the word loop, just label it as .endOfWord = True

    def search(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                # if, say, self.root as the first character, or first_char.children has
                # second character and so on, and if any point during this chain this
                # condition was not true, just return False
                return False
            curr = curr.children[c]
        return curr.endOfWord # else, just return whether the end of loop is endOfWord

    def startsWith(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True # whether in this case just return True (since we are only concerned with start)
