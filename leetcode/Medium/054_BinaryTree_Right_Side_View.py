from BTree_Lib import BinaryTree as BT
# using two list strategy, and only printing the rightmost value in current list (if present)
def binarytree_right_side_view(tree: BT):
    node_queue = [tree]
    while node_queue != []:
        next_queue = []
        for node in node_queue:
            if node.left is not None:
                next_queue.append(node.left)
            if node.right is not None:
                next_queue.append(node.right)
        if node_queue[-1].val is not None:
            print(node_queue[-1].val)
        node_queue = next_queue

tree = BT.create([1, 2, 3, 4, 5, 6, 7])
binarytree_right_side_view(tree)
