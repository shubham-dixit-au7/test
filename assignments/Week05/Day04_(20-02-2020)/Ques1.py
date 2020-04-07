#Question- https://www.geeksforgeeks.org/exchange-first-last-node-circular-linked-list/

#Answer- 
import math 
  
class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
def addIt(head, data): 
    if (head != None): 
        return head 
    temp = Node(data) 
    temp.data = data 
    head = temp 
    head.next = head 
    return head 
  
def addStart(head, data): 
    if (head == None): 
        return appendIt(head, data)   
    temp = Node(data) 
    temp.data = data 
    temp.next = head.next
    head.next = temp 
    return head 

def swapNodes(head): 
    p = head 
    while (p.next.next != head): 
       p = p.next 
    p.next.next = head.next
    head.next = p.next
    p.next = head 
    head = head.next
    return head 

def traversal(head):  
    if (head == None): 
        print("List is empty.") 
        return
    p = head 
    print(p.data, end = " ") 
    p = p.next
    while(p != head):
        print(p.data, end = " ") 
        p = p.next
  

   

head = None
head = appendIt(head, 6) 
for x in range(5, 0, -1): 
    head = addStart(head, x) 
print("Before: ", end = "") 
traversal(head) 
print()
print("After: ", end = "") 
head = swapNodes(head) 
traversal(head) 