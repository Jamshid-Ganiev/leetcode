class Queue:
    # initialize and empty list
    def __init__(self):
        self._qList = list()

    # Check if the queue is empty or not
    def isEmpty(self):
        return len(self._qList) == 0
    
    # return the lenght of the queue
    def __len__(self):
        return len(self._qList)
    
    # add a new item to the queue
    def enqueue(self, item):
        self._qList.append(item)

    # pop the first item from the queue
    def dequeu(self):
        assert not self.isEmpty(), 'Cannot dequeue from an empty queue'
        return self._qList.pop(0)
    
coffee_queue = Queue()
coffee_queue.enqueue('james')
coffee_queue.enqueue('Lara')
coffee_queue.enqueue('Donald')
coffee_queue.enqueue('Barak')

print(coffee_queue.isEmpty())
print(coffee_queue.__len__()) # 4
print('------')
print(f'Whose turn?\n>>{coffee_queue.dequeu()}')
print(coffee_queue.__len__()) # 3

print(f'Whose turn?\n>>{coffee_queue.dequeu()}')
print(coffee_queue.__len__()) # 2

# in the terminal:
# False
# 4
# ------
# Whose turn?
# >>james
# 3
# Whose turn?
# >>Lara
# 2
