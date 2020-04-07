#Question- Implement Stack using a linked list

#Answer- 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
# checking if the list is empty    

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
#  adding element to stack    

    def push(self,data):
        
        if self.head == None:
            self.head = Node(data)
        else:
            topNode = Node(data)
            topNode.next = self.head
            self.head = topNode
            
#     deleting elemrnt
#     It'll be deleted from the top

    def pop(self):
        if self.head == None:
            print("StackUnderflow")
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.data
        
    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.data
        
    
    def print_list(self):
        curr_node = self.head
        
        while curr_node is not None:
            print(str(curr_node.data)+" -> ",end="")  
            curr_node = curr_node.next  
        print("None") 
        
        
s = Stack() 

s.push(5)
s.push(8)
s.push(11)
s.push(14)

print("Initial Stack is: ", end="")
s.print_list()

top_elem = s.peek()
print("Top element is ", top_elem)

# pop_elem = s.pop() 
# print("Popped element is ", pop_elem)

# pop_elem = s.pop() 
# print("Popped element is ", pop_elem)

# pop_elem = s.pop() 
# print("Popped element is ", pop_elem)

pop_elem = s.pop() 
print("Popped element is ", pop_elem)

print("Current Stack is: ", end="")
s.print_list()

# solution 2

[20:33, 28/02/2020] Anik AttainU: class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None
        self.end = None

    def push(self, data):
        if self.head is None:
            temp_node = Node(data)
            temp_node.next = self.head
            self.head = temp_node
            self.end = temp_node
        else:
            temp_node = Node(data)
            temp_node.next = self.head
            self.head = temp_node
        return

    def pop(self):
        if self.head is None:
            return None
        temp_node = self.head
        self.head = self.head.next
        return temp_node


class Stack:
    def _init_(self, max_size=100):
        self.stack = LinkedList()
        self.max_size = max_size
        self.curr_size = 0

    def push(self, data):
        if self.max_size > self.curr_size:
            self.stack.push(data)
            self.curr_size += 1

    def pop(self):
        if self.curr_size <= 0:
            return None
        x = self.stack.pop()
        self.curr_size -= 1
        return x

    def peek(self):
        if self.curr_size <= 0:
            return None
        else:
            return self.stack.end

    def isEmpty(self):
        if self.curr_size <= 0:
            return True
        return False

    def display(self):
        current_node = self.stack.head
        print("<==>", end="")
        while current_node:
            print('\033[46m', current_node.data, '\033[41m', end=" --\033[0m-->")
            current_node = current_node.next
        else:
            print('\033[44m', "None", '\033[0m', end="")
            print()
            print()


stk = Stack()
list1 = "18 5 11 30 19 5 6 2 3"
for i in list1.split():
    stk.push(int(i))
print()
print("Input Stack : ", end="")
stk.display()
print("First elem to come out of the stack, is the last elem of the input : ", stk.pop().data)
print()
print("Modified Stack : ", end="")
stk.display()
print("Peek Element : ", stk.peek().data)
print()
print("Stack is empty : ", stk.isEmpty())
[20:34, 28/02/2020] Anik AttainU: # Implement Stacks using Queues


class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None
        self.end = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.end = self.head
            return

        else:   # to append in O(1)
            self.end.next = Node(data)
            self.end = self.end.next

    def pop(self):
        if self.head is None:
            return None
        curr_node = self.head
        self.head = self.head.next
        return curr_node


class Queue:
    def _init_(self, max_size=100):
        self.queue = LinkedList()
        self.front = self.rear = -1
        self.max_size = max_size

    def enqueue(self, data):
        if self.rear < self.max_size:
            self.queue.append(data)
            self.rear += 1
            if self.front == -1:
                self.front += 1

    def deque(self):
        if self.front == -1:
            return None
        else:
            x = self.queue.pop()
        if self.rear == 0:
            self.front = self.rear = -1
        else:
            self.rear -= 1
        return x

    # def front_elem(self):
    #     if self.front == -1:
    #         return None
    #     else:
    #         return self.queue.head.data

    # def rear_elem(self):
    #     if self.rear != -1:
    #         return self.queue.end.data
    #
    # def isEmpty(self):
    #     if self.front == -1:
    #         return True
    #     return False

    def pop(self):
        return self.deque().data

    def list_append(self, data):
        return self.enqueue(data)

    def get_size(self):
        curr_node = self.queue.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def display(self):
        current_node = self.queue.head
        print("deque <--", end="")
        while current_node:
            print('\033[46m', current_node.data, '\033[41m', end=" --\033[0m-->")
            current_node = current_node.next
        else:
            print('\033[44m', "None", '\033[0m', end="")
            print("<-- enqueue")
            print()


que = Queue()
list1 = "18 5 11 30 19 5 6 2 3"
for i in list1.split():
    que.enqueue(int(i))
print()
print("Input Queue : ", end="")
que.display()
size = que.get_size()
for i in range(size - 1):
    x = que.pop()
    que.list_append(x)
print("stack implementation using queue : ", end="")
que.display()
print("Now the first element to pop from the stack i.e the last element of the queue is : ", que.pop())