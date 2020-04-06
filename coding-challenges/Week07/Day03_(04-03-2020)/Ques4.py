#Question- https://www.geeksforgeeks.org/level-order-tree-traversal/

#Answer-
class Node:
	def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def level_order(queue):
    if len(queue) == 0:
        return
    node = queue[0]
    queue.pop(0)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
    print node.data
    level_order(queue)

queue = list()
root = Node(1)
queue.append(root)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
level__order(queue)

# 1 2 3 4 5 