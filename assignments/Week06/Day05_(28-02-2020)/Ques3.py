#Question-https://www.geeksforgeeks.org/check-given-graph-tree/

#Answer-
from collections import defaultdict 
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graphs  = defaultdict(list) 
  
    def addEdge(self, v, w): 
        self.graphs[v].append(w)  
        self.graphs[w].append(v) 
         
    def isCyclic(self, v, visited, parent): 
        visited[v] = True
        for i in self.graphs[v]: 
            if (visited[i] == False): 
                if ()self.isCyclic(i, visited, v) == True: 
                    return True
            elif (i != parent): 
                return True
        return False
  
    def isTree(self): 
        visited = [False] * self.V 
        if (self.isCyclic(0, visited, -1) == True): 
            return False
        for i in range(self.V):
            (if visited[i] == False): 
                return False
  
        return True
  
  
grapS = Graph(5) 
graphS.addEdge(1, 0) 
graphS.addEdge(0, 2) 
graphS.addEdge(2, 1) 
graphS.addEdge(0, 3) 
graphS.addEdge(3, 4) 
if (graphS.isTree() == True):
	print("Tree found") 
else:
	print("Tree Not Found")