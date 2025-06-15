# We create a special Node class, called SNode, for the purpose of this project
class SNode:
    def __init__(self):
        self.val = None
        self.next = None
        # a 'random' instantce variable that would hold the index of where we are trying to look at
        self.random = None

    @staticmethod
    def from_vals(vals: list[list[int | None]]):
        root = SNode()
        tail = root
        for val, rnd in vals:
            tail.val = val
            # if rnd is not None, then use this as index to our vals list, and take the first, val value
            # else have it as None only
            tail.random = vals[rnd][0] if rnd is not None else None
            # creating a tail node so that it won't be None
            tail.next = SNode()
            tail = tail.next
        return root

    def len(self) -> int:
        len = 0
        while self is not None:
            len += 1
            self = self.next
        return len - 1

    def to_vals(self) -> list[list[int | None]]:
        vals = []
        root = self
        tail = root
        # first caching all the values in an array, so that it can be indexed
        while tail.next is not None:
            vals.append(tail.val)
            tail = tail.next
        res = []
        tail = root # making tail begin at the beginning again
        while tail.next is not None:
            if tail.random is None: # if our random is None, merely appened None
                res.append([tail.val, None])
            else:
                # finding where exactly does the index is which have the value tail.random
                random_inx = 0
                while random_inx < len(vals) and vals[random_inx] != tail.random:
                    random_inx += 1
                res.append([tail.val, random_inx])
            tail = tail.next
        return res

n = SNode.from_vals([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
print(n.to_vals())
