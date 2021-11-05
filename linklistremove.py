class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None

    def at_begin(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    def remove_node(self, remove_key):

        val = self.head

        if val is not None:
            if val.data == remove_key:
                val.next = None
                return

        while val is not None:
            if val.data == remove_key:
                break
            prev = val
            val = val.next

        if val is None:
            return

        prev.next = val.next

        val.next = None

    def list_print(self):
        print_val = self.head
        while print_val:
            print(print_val.data),
            print_val = print_val.next


list1 = Slinkedlist()
list1.at_begin("monday")
list1.at_begin("tuesday")
list1.at_begin("wednesday")
list1.at_begin("thursday")
list1.list_print()
print("\n")
list1.remove_node("tuesday")
list1.list_print()


