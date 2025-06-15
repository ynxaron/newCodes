from BTree_Lib import BinaryTree as BT

# I do not understand exactly how this solution works
def construct(preorder: list[int], inorder: list[int]) -> BT | None:
    if not preorder or not inorder:
        return None

    tree = BT.create([preorder[0]])
    mid = inorder.index(preorder[0])

    tree.left  = construct(preorder[1:mid+1], inorder[:mid])
    tree.right = construct(preorder[mid+1:], inorder[mid+1:])
    return tree

tree = BT.create([12, 8, 15, 4, 9, 13, 18])
tree.print()
#print("Inorder:  " + str(tree.to_inorder()))
#print("Preorder: " + str(tree.to_preorder()) + "\n")
new_tree = construct(tree.to_preorder(), tree.to_inorder())
new_tree.print() if new_tree is not None else print('X')
