#Question- Implement Queues using Stacks

#Answer- 
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None
        # self.end = None

    def push(self, data):
        if self.head is None:
            temp_node = Node(data)
            temp_node.next = self.head
            self.head = temp_node
            # self.end = temp_node
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

    def isEmpty(self):
        if self.curr_size <= 0:
            return True
        return False


class Queue:
    push_stack = Stack()
    pop_stack = Stack()

    def enqueue(self, data):
        Queue.push_stack.push(data)

    def deque(self):
        if Queue.pop_stack.isEmpty():
            if Queue.push_stack.isEmpty():
                return None
            else:
                for _ in range(Queue.push_stack.curr_size):
                    x = Queue.push_stack.pop()
                    Queue.pop_stack.push(x)
        result = Queue.pop_stack.pop()
        return result.data


que = Queue()
list1 = "5 11 5 6 2 3"
for i in list1.split():
    print("Enqueueing : %d" % int(i))
    que.enqueue(int(i))
print()
for _ in range(4):
    x = que.deque()
    if x:
        print("De-queueing : %d" % x.data)
    else:
        print("De-queueing : Queue is Empty")
        break
print()
list1 = "8 4 9 5 7"
for i in list1.split():
    print("Enqueueing : %d" % int(i))
    que.enqueue(int(i))
print()
for _ in range(20):
    x = que.deque()
    if x:
        print("De-queueing : %d" % x.data)
    else:
        print("De-queueing : Queue is Empty")
        break