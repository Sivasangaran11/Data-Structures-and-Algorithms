class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        new_node.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            if temp.data == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
        if temp.data == data:
            prev.next = temp.next

    def print_list(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.prepend(0)
cll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> (head)
cll.delete(2)
cll.print_list()  # Output: 0 -> 1 -> 3 -> (head)
cll.delete(0)
cll.print_list()  # Output: 1 -> 3 -> (head)
