class Stack:
    MAX_SIZE = 10
    def __init__(self):
        self.data = []
    def is_full(self):
        return len(data) == MAX_SIZE
    def is_empty(self):
        return len(data) == 0
    def push(self, item):
        if self.is_full():
            print('FULL DATA')
        else:
            self.data.append(item)
            print('SUCCESS - push method')
    def pop(self):
        if self.is_empty():
            print('EMPTY')
            return None
        else:
            print('SUCCESS - pop method')
            return self.data.pop()

class Simple_Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
        print('SUCCESS - push method')
    def pop(self):
        if len(self.data == 0):
            print('EMPTY')
            return None
        else:
            print('SUCCESS - pop method')
            return self.data.pop()

# 사실 stack은 리스트([]), pop(), append(), len() 함수의 조합만으로 구현 가능
