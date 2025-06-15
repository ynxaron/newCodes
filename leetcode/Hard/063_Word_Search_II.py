class TrieNode:
    def __init__(self):
        self.children  = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    @staticmethod
    def check_words(board: list[list[str]], words: list[str]) -> list[str]:
        lrow, lcol = len(board), len(board[0])
        indeces_seen = set() # all the indeces that we have seen before, usefull in backtracking
        def develop_from(curr: TrieNode, i: int, j: int):
            # if the indeces are invalid
            if (i < 0 or i >= lrow) or (j < 0 or j >= lcol):
                return
            # if this pair of indeces are already seen, (because we can't take duplicates)
            if ((i, j) in indeces_seen):
                return
            this_char = board[i][j]
            # prepending and forwarding our TrieNode()
            if this_char not in curr.children:
                curr.children[this_char] = TrieNode()
            curr = curr.children[this_char]
            indeces_seen.add((i, j))
            # checking all four possibilities. Whenever the indeces would be invalid, it would return instantly
            develop_from(curr, i + 1, j)
            develop_from(curr, i - 1, j)
            develop_from(curr, i, j + 1)
            develop_from(curr, i, j - 1)

            # then removing the indeces becase, say we took the horizontal path, increased (i + 1)
            # but found out there is no answer there. Then if we took (j + 1), we would still like
            # to possibly include (i + 1, j) within our new path since are beginning another
            # traversal. The point of indeces_seen was not to include the same indeces within a singular
            # traversal
            indeces_seen.remove((i, j))

        curr = Trie() # a Trie() that we would be maintaining throughout the code
        found_words = [] # a collection of all the words that have been 'found' in our Trie()
        winx = 0 # words inx
        while winx < len(words):
            for i in range(lrow):
                for j in range(lcol):
                    # we have beginning of a word, which means
                    # rest of the word could be build from it
                    if board[i][j] == words[winx][0]:
                        develop_from(curr.root, i, j)
                        # if the word is in the developed Trie, and if the word is not
                        # already in found_words list,then append it to the list
                        if curr.search(words[winx]):
                            found_words.append(words[winx])
                            # if curr.search returns positive, then we simply move on to next
                            # word (since we must move on to next word in two conditions, either
                            # in one of our searches results positive, or none did)
                            winx += 1
                            continue
                    curr = Trie()
            winx += 1

        return found_words

# trie = Trie()
# board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
# words = ["oath", "pea", "eat", "rain"]
# print(trie.check_words(board, words))
