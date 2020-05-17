class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, start):
        self.start = start 

    def get(self, index):
        node = self.start
        for i in range(index): 
            node = node.next
        return node

    def add_beginning(self, data):
        self.start = Node(data, self.start)
        return

    def add(self, index, data):
        #old add
        if index == 0:
            self.add_beginning(data)
            
        #as an example assume we want to append after index 1 the value 20...
        #We would move the previous node.next to this new node.next.
        #previous node.next to point to the new node. 
        node = self.start #consider index 0. 
        for i in range(index-1): #-1 to get before that node 
            node = node.next
        node.next = Node(data, next_node=node.next)

    def add(self, index, data):
        if index == 0:
            self.add_beginning(data)

        node = self.get(index-1)
        node.next = Node(data, node.next)

    def append(self, data):
        node = self.start
        while True:
            if not node.next:
                break
            node = node.next
        node.next = Node(data)

    def delete(self, index):
        #old delete
        node = self.start
        for i in range(index-1): #stop one befere the node as you gotta update next
            node = node.next
        node.next = node.next.next

    def delete_beginning(self):
        print("self.start:", self.start, self.start.next)
        self.start = self.start.next

    def delete(self, index):
        if index == 0:
            self.delete_beginning()
            return
        print("new delete")
        node = self.get(index-1) #get before
        node.next = node.next.next

    def __repr__(self):
        string = ''
        node = self.start
        while True:
            string += str(node) + " "
            if not node.next:
                break
            node = node.next
        return string

linked_list = LinkedList(Node(10))
linked_list.start.next = Node(20)
linked_list.start.next.next = Node(30)
linked_list.add(3, 40)
print(linked_list)
linked_list.delete(0)
print(linked_list)
