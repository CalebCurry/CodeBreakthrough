class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, start):
        self.start = start

linked_list = LinkedList(Node(10))
linked_list.start.next = Node(20)
linked_list.start.next.next = Node(30)

print(linked_list.start.next.next.data)
