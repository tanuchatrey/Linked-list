class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def sortedMerge(head1, head2):
    arr = []  

    # pushing the values of the first linked list
    while head1 is not None:
        arr.append(head1.data)
        head1 = head1.next

    # pushing the values of the second linked list
    while head2 is not None:
        arr.append(head2.data)
        head2 = head2.next

    # sorting the list
    arr.sort()

    # creating a new list with sorted values
    dummy = Node(-1)
    curr = dummy

    for value in arr:
        curr.next = Node(value)
        curr = curr.next

    return dummy.next 

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

if __name__ == "__main__":
  
    head1 = Node(5)
    head1.next = Node(10)
    head1.next.next = Node(15)
    head1.next.next.next = Node(40)

    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)

    res = sortedMerge(head1, head2)

    printList(res)
