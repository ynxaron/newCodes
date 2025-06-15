# The crux of this algorithm is to simply search node
# by node which one, left node or right node, is the smaller
# Then append that smaller to the tail, and increment that node which
# was smaller to it's right
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    @staticmethod
    def create(val: list[int]):
        node = Node(val[0])
        root = node
        for v in val[1:]:
            n = Node(v)
            node.next = n
            node = node.next
        return root

    def to_string(self) -> str:
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} --> {self.next.to_string()}"

    def print(self):
        print(self.to_string())

def merge_two_sorted_list(l: Node , r: Node) -> Node:
    if l.val > r.val:
        root = r
        r = r.next
    else:
        root = l
        l = l.next

    root.next = None # breaking previous bonds
    tail = root # using a tail node so we don't have to do O(n) everytime we are appending
    while l is not None and r is not None:
        if l.val > r.val:
            tail.next = Node(r.val)
            tail = tail.next # incrementing the tail node
            r = r.next
        else:
            tail.next = Node(l.val)
            tail = tail.next
            l = l.next

    while l is not None: # if one of the node still have some numbers left
        tail.next = Node(l.val)
        tail = tail.next
        l = l.next

    while r is not None:
        tail.next = Node(r.val)
        tail = tail.next
        r = r.next
    return root

l = Node.create([1, 4, 5, 6, 7])
r = Node.create([2, 6, 8, 10, 12])

merge_two_sorted_list(l, r).print()
