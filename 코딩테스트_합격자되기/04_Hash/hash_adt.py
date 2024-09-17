from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

# https://kjw1313.tistory.com/78
class HashTable:
    # 초기화
    def __init__(self, SIZE=1000):
        self.SIZE = SIZE
        self.table = defaultdict(ListNode)
    
    # 삽입
    def put(self, key, value):
        index = key % self.SIZE

        # index에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # index에 노드가 존재하는 경우 연결리스트 처리
        data = self.table[index]
        while data:
            if (data.key == key):
                data.value = value
                return
            if (data.next is None):
                break
            data = data.next
        data.next = ListNode(key, value)
    
    # 조회
    def get(self, key):
        index = key % self.SIZE
        if self.table[index].value is None:
            return None
        
        data = self.table[index]
        while data:
            if (data.key == key):
                return data.value
            data = data.next
        return None
    
    # 삭제
    def remove(self, key):
        index = key % self.SIZE
        if self.table[index].value is None:
            return None
        
        # index의 첫 번째 노드일 때 삭제
        data = self.table[index]
        if (data.key == key):
            self.table[index] = data.next if data.next else ListNode()
            return
        
        # 연결 리스트 중 하나일 때 삭제
        prev = data
        data = data.next
        while data:
            if data.key == key:
                prev.next = data.next
                return
            prev, data = data, data.next
            