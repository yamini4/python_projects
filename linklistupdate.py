# linked list is a sequence of data elements
# which are connected together via links.
# each data elements contains a connection to another data element in form of a pointer
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        val = self.head
        while val is not None:
            print(val.data, end=" ")
            val = val.next

# update the new nodes next val to existing node

    def atbegining(self, new_data):
        NewNode = Node(new_data)
        NewNode.next = self.head
        self.head = NewNode

# Function to add new node
    def atend(self, new_data):
        New_node = Node(new_data)
        if self.head is None:
            self.head = New_node
            return
        last1 = self.head
        while last1.next:
            last1 = last1.next
        last1.next = New_node


list1 = SLinkedList()
list1.head = Node("monday")
e2 = Node("tuesday")
e3 = Node("wednesday")

# link first node to second node
list1.head.next = e2

# link second node to third node
e2.next = e3
print("list before update:\t", end=" ")
list1.listprint()
# adding node at beginning
list1.atbegining("sunday")
# adding node at ending
list1.atend("thursday")
print("\n")
print("updated list:\t", end=" ")
list1.listprint()
