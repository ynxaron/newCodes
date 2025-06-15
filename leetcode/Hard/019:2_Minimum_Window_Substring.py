# We would be using a class called 'Record', that would have three methods and one
# initializing method
class Record:
    def __init__(self, key): # since the record of our 'key' is the same, this is
        self.key_map = {} # what we would be initializing it with
        self.window_map = {}
        self.matched = 0 # a variable that would keep track if in our window there is a key
        for c in key: # initializing the key
            self.key_map[c] = 1 + self.key_map.get(c, 0)

    def is_valid(self): # checking whether in our substring there is a 'key'
        return self.matched == len(self.key_map)

    def increment(self, c):
        if c in self.key_map: # ignoring all those elements that are not in key
            self.window_map[c] = 1 + self.window_map.get(c, 0)
            # matching will be incremented with 1 if we have exactly as much a single character as needed
            self.matched += 1 if self.window_map[c] == self.key_map[c] else 0

    def decrement(self, c):
        if c in self.key_map:
            if self.window_map[c] == self.key_map[c]:
                # if we have exactly as much a single character as needed,
                # and now one of them, this, is going, we must decrease `matched`
                self.matched -= 1
            self.window_map[c] -= 1

def minimum_window_substring(inp: str, k: str) -> str:
    if inp == "": return ""
    record = Record(k) # initializing the record
    min_len, min_range = float("inf"), [-1, -1]
    l = 0
    for r in range(len(inp)):
        record.increment(inp[r])
        while record.is_valid(): # this loop would initialize only when in our current substring, there is key
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                min_range = [l, r]
            record.decrement(inp[l]) # decrement our record by inp[l]
            l += 1


    min_l, min_r = min_range
    return inp[min_l:min_r+1] if min_len != float("inf") else ""

print(minimum_window_substring("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("HCMALCITAM", "CAT"))
