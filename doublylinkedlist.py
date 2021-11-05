# doubly linked list contains a link element called first and list
# each link carries a data fields and two link fields called next and prev
# each link is linked with its next link using its next link
# each link is linked with its previous link using its previous link
# the last link carries a link as null to mark the end of the list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

# Adding data elements
    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

# print the doubly linked list
    def listprint(self, node):
        while node is not None:
            print(node.data, end=" "),
            last = node
            node = node.next


dllist = DoublyLinkedList()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)


