
class Queue:
    # Creates an empty array
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self._count = 0
        self._front = 0
        self._back = self.maxSize - 1
        self._qArray = [None] * self.maxSize

    # returns True if the queue is empty
    def isEmpty(self):
        return self._count == 0
    
    # returns True if the queue is full
    def isFull(self):
        return self._count == self.maxSize
    
    # return the lenght of the queue
    def __len__(self):
        return self._count
    
    # adds the given item to the queue if not full
    def enqueue(self, item):
        # assert statment raises an error if isFull() returns True as "NOT TRUE --> FALSE"
        assert not self.isFull(), "Cannot enqueue to a full queue."
        self._back = (self._back + 1) % self.maxSize
        self._qArray[self._back] = item
        self._count += 1
        print(f"{item} was added successfully")

    # removes and returns the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[self._front]
        self._front = (self._front + 1) % self.maxSize
        self._count -= 1
        return item
    
    # prints the current state of the queue
    def __str__(self):
        return str(self._qArray)
    

waffleQueue = Queue(6)

# Enqueuing 3 items:
waffleQueue.enqueue('James')
waffleQueue.enqueue('Bob')
waffleQueue.enqueue('Amanda')

# checking the state:
print(waffleQueue.__str__())

# dequeuing 1 item:
print(f"dequeued item: {waffleQueue.dequeue()}")

# results:
# James was added successfully
# Bob was added successfully
# Amanda was added successfully
# ['James', 'Bob', 'Amanda', None, None, None]
# dequeued item: James