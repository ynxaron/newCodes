from BTree_Lib import BinaryTree as BT
# The crux of this algorithm is to use a simple
# level wise travel as convering it from tree, to array
# array to then a string, then a string back to an array,
# then array back to a tree
def serialize_and_deserialize():
    def serialize(tree: BT) -> str:
        # using a queue data structure to convert a tree to an array
        array: list[int | None] = []
        q: list[BT | None] = [tree]
        while q:
            curr = q.pop(0)
            if curr is not None and curr.val is not None:
                array.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            else:
                array.append(None)
        return str(array) # returning a stringed version of array

    def deserialize(init_str: str) -> BT:
        init = []
        # Ignoring the '[' and ']' that would be present at first and last point
        for s in init_str[1:len(init_str)-1].split(','):
            try:
                int(s) # if succeded, then simply append the converted value
                init.append(int(s))
            except:    # else simply just append None, which would be the only thing left
                init.append(None)

        tree = BT()
        q: list[BT | None] = [tree]
        for v in init:
            curr = q.pop(0)
            curr.val = v
            # appending the left and right value to our current queue
            curr.left = BT()
            curr.right = BT()
            q.append(curr.left)
            q.append(curr.right)
        return tree

    return serialize, deserialize

#tree = BT.create([6, 3, 4, 7, 5, 2])
#tree.print()
#ser, des = serialize_and_deserialize()
#des(ser(tree)).print()
