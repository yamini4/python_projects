# stacks, queues, trees, hashMaps, graphs, linked-list

# stacks are made from arrays
# stacks follow the LIFO(Last In First Out) principle
# They have a pointer called TOP which is to track the top of the element
# PUSH: this is the push operator where data is added into the stack
# POP: this is the pop operation where the data is deleted from the stack

# example

stack = []

def empty():
    if len(stack) == 0:
        print("stack is empty.\n")
    else:
        print(stack, "\n")


val1, val2, val3 = 1, 2, 3
stack.append(val1)
stack.append(val2)
stack.append(val3)
empty()
a = stack.pop()
b = stack.pop()
c = stack.pop()

print("The popped elements are:", a, b, c, "\n")


# defining class
...
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()
while True:
    print("1) push\n2) pop\n3) Quit\n")
    do = int(input("what would you like to do?:"))
    if do == 1:
        val = input("enter the value: ")
        s.push(val)
    elif do == 2:
        if s.is_empty():
            print("stack is empty")
        else:
            print("popped value: ", s.pop())
    elif do == 3:
        break
    elif do >= 3:
        print("wrong input")
