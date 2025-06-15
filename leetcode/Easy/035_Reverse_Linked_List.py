# We can reverse a linked list by two methods.
# Let us take an example list: 1 -> 2 -> 4 -> 7 -> 9
# Recursivly, we can reverse (2 -> 4 -> 7 -> 9), it becomes
# (9 -> 7 -> 4 -> 2), then, since we would have two pointers,
# one at 9, and other at 2, then we append end.next = Node,
# node.next = None, hence making it 9 -> 7 -> 4 -> 2 -> 1
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def to_string(self) -> str:
        if self.next is None:
            return f"{self.val}"
        return f"{self.val} -> {self.next.to_string()}"

    def print(self):
        print(self.to_string())

    @staticmethod
    def append_list(vals: list[int]):
        node = Node(vals[0])
        root = node
        for v in vals[1:]:
            node.next = Node(v)
            node = node.next
        return root

    def reverse(self):
        prev, curr = None, self
        while curr:
            next = curr.next # we take the next value
            curr.next = prev # we make the curr.next point backwards
            prev = curr # we make prev current
            curr = next # we make curr next
        return prev # returning the previous node because this is where it would end, with curr = None

    @staticmethod
    def reverse_rec(node):
        if node.next is None:
            return node, node

        root, end = Node.reverse_rec(node.next) # we have two pointers, one at the beginning, one at end
        node.next = None
        end.next = node  # we append this value at the end, since we are reversing it
        end = end.next   # we are updating the end value
        return root, end # returning the root, end pair

print("BEFORE REVERSE: ")
node = Node.append_list([1, 2, 3, 4, 5])
node.print()
print("AFTER FIRST PREVERSE: ")
node = node.reverse()
node.print()
print("AFTER SECOND REVERSE: ")
node, _ = Node.reverse_rec(node)
node.print()
