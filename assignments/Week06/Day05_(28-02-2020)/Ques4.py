#Question-https://www.geeksforgeeks.org/check-given-graph-tree/

#Answer-
class Node: 
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None
  
def dispRtL(root): 
    if (root == None):  
        return
    stack = [] 
    stack.append(root)  
    parent = {}  
    parent[root] = None
    while len(stack) != 0: 
        current = stack[-1] 
        stack.pop(-1)   
        if (not (current.left) and
            not (current.right)):  
            displayTtBPath(current, parent)  
        if (current.right): 
            parent[current.right] = current  
            stack.append(current.right) 
        if (current.left): 
            parent[current.left] = current  
            stack.append(current.left) 

def displayTtBPath(curr, parent): 
    stk = []  
    while (curr): 
        stk.append(curr)  
        curr = parent[curr] 
    while len(stk) != 0: 
        curr = stk[-1]  
        stk.pop(-1)  
        print(curr.data, end = " ") 
    print() 

root = Node(10)  
root.left = Node(8)  
root.right = Node(2)  
root.left.left = Node(3)  
root.left.right = Node(5)  
root.right.left = Node(2)  
dispRtL(root) 