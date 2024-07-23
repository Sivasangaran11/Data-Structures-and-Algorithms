class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + "->"
            itr = itr.next
        print(listr)
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        temp = self.head
        while count < index - 1:
            temp = temp.next
            count += 1
        node = Node(data, temp.next)
        temp.next = node
        if node.next is None:
            self.tail = node

ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.print()  # Output: 1->2->3->


'''
Pros:

O(1) Insertion: Inserting at the end of the list is constant time since you have a tail pointer that directly points to the last node.
Efficient: Suitable for scenarios where you frequently insert at the end.
Cons:

Extra Memory: Requires additional memory to store the tail pointer.
Slightly More Complex: The implementation is slightly more complex due to maintaining the tail pointer.'''