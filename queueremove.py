class Queue:
    def __init__(self):
        self.queue = list()

# insert method to add element
    def add_to_q(self, data_val):
        if data_val not in self.queue:
            self.queue.insert(0, data_val)
            return True
        return False

# pop method to remove element
    def remove_element(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "no elements in Queue!"


queue1 = Queue()
queue1.add_to_q("monday")
queue1.add_to_q("tuesday")
queue1.add_to_q("wednesday")
print(queue1.remove_element())
print(queue1.remove_element())

