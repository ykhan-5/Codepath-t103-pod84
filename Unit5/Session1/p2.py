class MyQueue:

    def __init__(self):
        self.stack1 = [] #Queue
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.push(self.stack1.pop())

        self.stack1.push(x)

        while self.stack2:
            self.stack1.push(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return self.stack1

myQueue = MyQueue()
myQueue.push(1); #// queue is: [1]
myQueue.push(2); #// queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); #// return 1
myQueue.pop(); #// return 1, queue is [2]
myQueue.empty(); #// return false

    