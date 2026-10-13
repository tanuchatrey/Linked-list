class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def reverseList(head):

    curr = head
    prev = None

    # traverse all the nodes of Linked List
    while curr is not None:

        # store next
        nextNode = curr.next

        # reverse current node's next pointer
        curr.next = prev

        # move pointers one position ahead
        prev = curr
        curr = nextNode

    return prev


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = reverseList(head)
    printList(head)
