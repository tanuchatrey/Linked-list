# Node class
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to delete Nth node from end
def deleteNthNodeFromEnd(head, n):

    if head is None:
        return head

    k = 0

    curr = head

    # Find length of linked list
    while curr is not None:
        curr = curr.next
        k += 1

    # If n is greater than length
    if n > k:
        return head

    # If head node needs to be deleted
    if k - n == 0:
        head = head.next
        return head

    # Reach node just before target node
    curr = head

    for i in range(1, k - n):
        curr = curr.next

    # Delete target node
    curr.next = curr.next.next

    return head


# Function to print linked list
def printList(head):

    curr = head

    while curr is not None:
        print(curr.data, end=" ")

        curr = curr.next


# Driver Code
if __name__ == "__main__":
    head = Node(1)

    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Function call
    head = deleteNthNodeFromEnd(head, 2)

    # Print updated linked list
    printList(head)
