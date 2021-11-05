# FIFO(queues follows first in first out rule)

class Queue:
    def __init__(self):
        self.queue = list()

# insert method to add element
    def add_to_q(self, data_val):
        if data_val not in self.queue:
            self.queue.insert(0, data_val)
            return True
        return False

    def size(self):
        return len(self.queue)


queue1 = Queue()
queue1.add_to_q("monday")
queue1.add_to_q("tuesday")
queue1.add_to_q("wednesday")
print(queue1.size())

