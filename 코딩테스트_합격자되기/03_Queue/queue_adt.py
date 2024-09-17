from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()
    
    def enqueue(self, x):
        self.data.append(x)
    
    def dequeue(self):
        return self.data.popleft()

class Simple_Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        return self.data.pop(0)

    def front(self):
        return self.data[0]
    
    def rear(self):
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data == 0)
    
    def show(self):
        print(self.data)

# https://codingsmu.tistory.com/123
class Circular_Queue:
    def __init__(self, MAX_SIZE=100):
        self.rear = 0
        self.front = 0
        self.queue = [0 for i in range(self.MAX_SIZE)]

    def is_empty(self):
        # 데이터 삽입 시 rear 증가, 데이터 꺼낼 시 front 증가하므로
        # rear와 front가 일치한다면 데이터가 없다는 것
        if self.rear == self.front:
            return True
        return False

    def is_full(self):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            # 포화상태의 경우 rear는 front의 한칸 뒤에 있음
            # 또한 front가 가리키는 위치는 항상 비어 있음
            return True
        return False
    
    def enqueue(self, x):
        if is_full():
            print("ERROR: FULL")
            return
        self.rear = (self.rear + 1) % (self.MAX_SIZE)
        self.queue[self.rear] = x
    
    # 큐는 선입선출이므로 앞에서 삭제가 이뤄져야 함
    # 따라서, rear 값의 변경이 없고 front를 +1 하며 데이터를 삭제
    def dequeue(self):
        if is_empty():
            print("ERROR: EMPTY")
            return
        self.front = (self.front +1) % MAX_SIZE
        return self.queue[self.front]
    
    def show(self):
        i = self.front
        if is_empty():
            print("EMPTY QUEUE")
            return
        while True:
            i = (i+1) % self.MAX_SIZE
            print(self.queue[i], ' ')
            if i == self.rear:
                break