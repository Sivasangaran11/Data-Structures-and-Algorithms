class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue : 
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return True if self.front is None else False
    def getFront(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    def getNext(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = self.front.next
        if(self.front == None):
            self.rear = None
        return temp.data
    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def dequeue(self, data):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = self.front.next
        if(self.front == None):
            self.rear = None
        return temp.data
    def peek(self, data):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
#TC - O(1)
#SC - O(1)