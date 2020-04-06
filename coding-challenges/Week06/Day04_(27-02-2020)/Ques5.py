#Question- https://www.geeksforgeeks.org/check-if-two-trees-are-mirror/

#Answer-

class node:
    def __init__(self,value):
        self.value = value 
        self.left = None   
        self.right = None  

class binarytree:
    def __init__(self,root): 
        self.root= node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        else:
            print("Traversal type "+ traversal + " is not supported!!!")

    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal +=(str(start.value))
            traversal =self.inorder_print(start.right,traversal)
        return traversal

tree = binarytree(1)   
tree.root.left = node(2)     
tree.root.right = node(3)
tree.root.left.left = node(4)
tree.root.left.right = node(5)
tree.root.right.left = node(6)
tree.root.right.right = node(7)
x = tree.print_tree("inorder") 
print("Inorder of tree 1:="+x)

def reverse(str):
	return str[-1::-1]

tree = binarytree(1)   
tree.root.right = node(2)     
tree.root.left = node(3)
tree.root.right.left = node(5)
tree.root.right.right = node(4)
tree.root.left.left = node(7)
tree.root.left.right = node(6)
y=tree.print_tree("inorder")
print("Inorder of tree 2:="+y)
print("reverse of inorder of tree 2:="+reverse(y))
if(x == reverse(y)):
    print("Binary tree are mirror images of each other")
else:
    print("Not mirror images")