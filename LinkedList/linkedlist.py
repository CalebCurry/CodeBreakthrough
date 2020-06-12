class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    def __init__(self, start):
        self.start = start

    def __len__(self):
        node = self.start
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def get(self, index):
        node = self.start
        for i in range(index):
            node = node.next
        return node

    def index(self, data):
        index = 0
        for node in self:
            if node.data == data:
                return index
            index += 1
        return -1

        # Without __iter__:
        """
        node = self.start
        index = 0
        while node is not None:
            if node.data == data:
                return index
            index += 1
            node = node.next
        """

    def add_beginning(self, data):
        self.start = Node(data, self.start)

    def add(self, index, data):
        if index == 0:
            self.add_beginning(data)
            return

        node = self.get(index - 1)
        node.next = Node(data, node.next)

    def append(self, data):

        node = self.get(len(self) - 1)  # get last node
        node.next = Node(data)

        # Without get:
        """
        node = self.start
        while True:
            if not node.next:
                break
            node = node.next
        node.next = Node(data)
        """

    def delete_beginning(self):
        node_to_return = self.start
        self.start = self.start.next
        return node_to_return

    def delete(self, index):
        if index == 0:
            return self.delete_beginning()

        node = self.get(index - 1)  # get before
        node_to_return = node.next
        node.next = node.next.next
        return node_to_return

    def delete_end(self):
        return self.delete(len(self) - 1)

    def __repr__(self):
        string = ''
        node = self.start
        while True:
            string += str(node) + " "
            if node.next is None:
                break
            node = node.next
        return string

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __eq__(self, other):
        print(self, other)
        for index in range(len(self)):
            if self.get(index) != other.get(index):
                return False
        return True

########## CREATING A LINKED LIST ##########


# creating a linked list with one node
linked_list = LinkedList(Node(10))
linked_list.start.next = Node(20)
linked_list.start.next.next = Node(30)
print(linked_list)  # 10 20 30

# Creating a chain up front with __init__
# Each node can take a next argument
linked_list = LinkedList(Node(10, Node(20, Node(30, Node(40)))))
print(linked_list)  # 10 20 30 40

# You could pass in a a bunch of nodes directly to the LinkedList
# linked_list = LinkedList(Node(10), Node(20), Node(30), Node(40))
# This would work if you set up the __init__ method with a *nodes parameter
# And then linked each node
# Here's an example of how to create a function to take unlimited arguments:
# https://youtu.be/s3IvdkCq2_c?t=21473


########## Get a node by index ##########


print("Index 2:", linked_list.get(2))  # 30


########## Get length of linked list ##########


print("Length of linked list:", len(linked_list))  # 4
print("Last element:", linked_list.get(len(linked_list) - 1))  # 40
print("Length of empty list:", len(LinkedList(None)))
print("Length of one node:", len(LinkedList(Node(50))))


########## Adding to a linked list ##########

linked_list.add_beginning(5)
linked_list.add(0, 3)
print(linked_list)  # 3 5 10 20 30 40

linked_list.add(2, 7.5)
linked_list.add(len(linked_list), 50)  # append
linked_list.append(60)  # Also append
print(linked_list)  # 3 5 7.5 10 20 30 40 50 60


########## Removing from a linked list ##########


removed1 = linked_list.delete(0)  # 3. This removed beginning
removed2 = linked_list.delete_beginning()  # 5. This removes beginning
removed3 = linked_list.delete(3)  # 30
removed4 = linked_list.delete(5)  # 60. This removes end
popped = linked_list.delete_end()  # 50. This removes end

print("Removed:", removed1, removed2, removed3, removed4, popped)  # 3 5 30 60 50
print("Here's what's left:", linked_list)  # 7.5 10 20 40


########## Iterate through linked list ##########


for node in linked_list:
    print(node)


########## Search linked list for data ##########


print(linked_list.index(7.5), linked_list.index(1),
      linked_list.index(10), linked_list.index(40))  # 0 -1 1 3


########## compare nodes ##########


print(Node(10) == Node(10))  # This should be True


########## compare linked list ##########


linked_list1 = LinkedList(Node(10, Node(5, Node(3))))
linked_list2 = LinkedList(Node(10, Node(5, Node(3))))

print(linked_list1 == linked_list2)  # True

linked_list2.get(1).data = 6  # Change one

print(linked_list1 == linked_list2)  # False
