# 3.2.1.16 Queue aka FIFO: part 2

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








######## 3.2.1.15 LAB: Queue aka FIFO ########

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
