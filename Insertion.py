class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert node after a particular node
    def insert_after(self, previous_node, data):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp is not None:
            if temp.data == previous_node:
                new_node = Node(data)

                new_node.next = temp.next
                temp.next = new_node

                return

            temp = temp.next

        print("Node not found")

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
ll = LinkedList()

ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Before insertion:")
ll.display()

# Insert 25 after 20
ll.insert_after(20, 25)

print("After insertion:")
ll.display()
