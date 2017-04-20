class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        return self.first[0]



    def pop(self):
        if self.second == []:
            while len(self.first) > 0:
                self.second.append(self.first.pop())
        self.second.pop()
        if len(self.second) >0:
            while len(self.second) > 0:
                self.first.append(self.second.pop())

    def put(self, value):
        self.first.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:

        queue.pop()
    else:
        print queue.peek()


