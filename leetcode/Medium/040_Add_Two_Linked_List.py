from Node_Lib import Node
n = Node.create([2, 4, 3])
m = Node.create([5, 6, 4])
p = Node.from_num(n.to_num() + m.to_num())
p.print()
