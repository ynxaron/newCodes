from BTree_Lib import BinaryTree as BT
def kth_smallest_element_in_a_BST(tree: BT, k: int):
    return tree.to_inorder()[k - 1]

tree = BT.create([10, 6, 12, 4, 8, 11, 14, 3, 5, 7, 9, None, None, 13, 15])
print(kth_smallest_element_in_a_BST(tree, 3))
