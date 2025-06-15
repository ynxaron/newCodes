from Node_Lib import Node
def linked_list_cycle(n: Node) -> bool:
    # implementing a slow, fast pointer method to check whether at any point when two pointers
    # at different speed are initialized, if they would come together
    slow, fast = n, n
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # if the distance between slow and fast, which at beginning is (len(node) - 1),
                         # has been chased down
            return True
    return False
