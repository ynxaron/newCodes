from Node_Lib import Node
# The idea behind this approach is to use typical divide-n-conquer
# approach to solve this problem.
def merge_k_sorted_linked_list(lists: list[Node]) -> Node | None:
    if not lists or len(lists) == 0:
        return None
    def merge_k_sorted_recursive(l: int, r: int) -> Node:
        if l == r:
            return lists[l]

        m = (l + r) // 2
        ln = merge_k_sorted_recursive(l, m) # this return one half, solved
        rn = merge_k_sorted_recursive(m + 1, r) # this return other half, solved

        return merge_linked_list(ln, rn) # and then this merges them, sending it upwards

    m = merge_k_sorted_recursive(0, len(lists) - 1)
    return m.remove_nones() # removing a list of Nones that would be present


def merge_linked_list(n: Node, m: Node) -> Node:
    n_back, m_back = n, m # creating backup to restore values
    root = Node()
    tail = root
    while n.next is not None and m.next is not None: # to avoid the possibility where n is not None, but n.val is None
        if n.val < m.val:
            tail.val = n.val
            n = n.next
        else:
            tail.val = m.val
            m = m.next
        tail.next = Node()
        tail = tail.next

    while n is not None:
        tail.val = n.val
        tail.next = Node()
        tail = tail.next
        n = n.next

    while m is not None:
        tail.val = m.val
        tail.next = Node()
        tail = tail.next
        m = m.next

    n, m = n_back, m_back # restoring values (let's see if we would need them)
    return root

n1 = Node.create([3, 5, 6, 8, 10])
n2 = Node.create([4, 5, 5, 7, 8, 11])
n3 = Node.create([3, 5, 6, 6, 8])
n4 = Node.create([3, 5, 6, 8])

m = merge_k_sorted_linked_list([n1, n2, n3, n4])
m.print()
