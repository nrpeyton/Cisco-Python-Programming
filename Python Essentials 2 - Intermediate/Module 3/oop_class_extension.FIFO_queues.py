'''
                 3.2.1.15 LAB: Implementing Queue Class with FIFO Model

Estimated Time: 20-45 minutes
Difficulty: Easy/Medium

Objectives:
- Master class definition from scratch.
- Implement standard data structures as classes.

Scenario:
Implement the Queue class adhering to the FIFO (First In First Out) model. Utilise a list for storage and support:
1. put(element) - Appends element at the end of the queue.
2. get() - Removes and returns element from the front of the queue.

Guidelines:
- Employ a list for underlying storage.
- Implement QueueError, a custom exception for empty queue scenarios, derived from an appropriate base exception.

Expected Output:
1
dog
False
Queue error
'''


class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if len(self.queue) == 0:
            raise QueueError()
        
        val = self.queue[0]
        del self.queue[0]
        return val

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")








'''
                           3.2.1.16 LAB: Extending Queue Class Functionality - Part 2

Estimated Time: 15-30 minutes
Difficulty: Easy/Medium

Objectives:
- Advance skills in subclass definition.
- Introduce new functionality to an existing class structure.

Scenario:
Augment the Queue class with a method to check if the queue is empty. This method should be parameterless and:
- Return True if the queue is devoid of elements.
- Return False if the queue contains elements.

Expected Output:
1
dog
False
Queue empty
'''


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError



# sub-class of Queue
class SuperQueue(Queue):
    def __init__(self): # own constructor
        Queue.__init__(self) # parent's constructor
    def isempty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False # false if queued


que = SuperQueue() 
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
