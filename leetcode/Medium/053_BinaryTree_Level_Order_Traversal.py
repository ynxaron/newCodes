from BTree_Lib import BinaryTree as BT
# Using two list method such that we append left nodes, and right nodes to a new list,
# and then make this new list our original list, and continuing this till our new_list is none
def binarytree_level_order_traversal(tree: BT):
    node_queue = [tree]
    while node_queue != []:
        node_str = ""
        next_queue = []
        for node in node_queue:
            node_str += str(node.val)
            if node.left is not None:
                next_queue.append(node.left) #  updating our next_queue
            if node.right is not None:
                next_queue.append(node.right) # updating our next_queue
        print(node_str)
        node_queue = next_queue
