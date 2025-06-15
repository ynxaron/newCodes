from Node_Lib import Node
# We are using a positional_inx variable such that the node next
# to it is the node we want to remove. Then, if it is the last node,
# that is if (k == 1), then we simply make the previous, positional_node
# link to None, else we simply make positional_node.next equal positional_node.next.next
def remove_nth_element_from_end_of_list(node: Node, k: int):
    positioning_inx = node.len() - k - 1 # such that (node.len() - k) is where our element of interest is
    i = 0
    while i < positioning_inx: # this loop would end when i == positioning_inx
        node = node.next
        i += 1

    if k > 1: # if the element of interest is not last
        node.next = node.next.next # then we simply make the element point to it's neighbour
    else:
        node.next = None # else we simply make it point to None

n = Node.create([1, 2, 3, 4, 5])
remove_nth_element_from_end_of_list(n, 3)
n.print()
