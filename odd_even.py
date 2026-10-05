class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def divide(head):

    # Result list to hold even nodes
    resStart = None
    resEnd = None

    # Pointers for the original list
    curr = head
    prev = None

    # Move all even nodes from original
    # to result
    while curr is not None:

        # If current node is even
        if curr.data % 2 == 0:

            # Remove the current even node
            # from the original list
            if prev is not None:
                prev.next = curr.next
            else:
                # If the even node is at the head
                head = curr.next

            # Add the current even node to the result list
            if resStart is None:
                resStart = curr
                resEnd = resStart
            else:
                resEnd.next = curr
                resEnd = resEnd.next

            curr = curr.next

        # If the node is odd, just move to the next
        else:
            prev = curr
            curr = curr.next

    # If there are no even nodes, return
    # the original list
    if resStart is None:
        return head

    # Append the remaining original list
    # (odd nodes) to the result list
    resEnd.next = head

    # Return the result list (starting with even nodes)
    return resStart

# Driver Code
if __name__ == '__main__':

    # Creating linked list: 17->15->8->9->2->4->6
    head = Node(17)
    head.next = Node(15)
    head.next.next = Node(8)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(6)

    head = divide(head)

    curr = head
    while curr is not None:
        print(curr.data, end='' if curr.next is None else '->')
        curr = curr.next
