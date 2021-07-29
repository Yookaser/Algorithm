# 10845. 큐

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)
    
    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    
    def back(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

import sys

input = sys.stdin.readline

N = int(input())
queue = Queue()

for i in range(N):
    command = input().split()

    if command[0] == 'push':
        queue.push(command[1])
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.empty())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())