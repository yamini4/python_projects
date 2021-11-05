# PUSH,POP into stack
# LIFO(stacks follows last in first out concept)

class Stack:
    def __init__(self):
        self.stack = []

    # use list append method to push element in stack
    def push_element(self, data_val):
        if data_val not in self.stack:
            self.stack.append(data_val)
            return True
        else:
            return False
    # use pop to look at the top of the stack

    def pop_element(self):
        return self.stack[-1]


stack1 = Stack()
stack1.push_element("monday")
stack1.push_element("tuesday")
print(type(stack1))
print("$")
stack1.pop_element()
print(stack1.pop_element(), end="\n")
print("$")
stack1.push_element("wednesday")
stack1.push_element("thursday")
print(stack1.pop_element())






