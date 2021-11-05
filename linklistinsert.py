# inserting an element between two nodes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init___(self):
        self.head = None

# function to add node in the required position
    @staticmethod
    def in_bet(middle_node, new_data):
        if middle_node is None:
            print("the mentioned node is absent")
            return

        NewNode = Node(new_data)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

# print the linked list
    def list_print(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next


list1 = Slinkedlist()
list1.head = Node("monday")
e2 = Node("tuesday")
e3 = Node("thursday")

list1.head.next = e2
e2.next = e3

list1.in_bet(list1.head.next, "wednesday")

list1.list_print()



