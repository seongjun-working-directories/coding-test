'''
[문제 027]
첫 번째 인수 lst를 이용하여 이진 탐색 트리를 생성하고,
두 번째 인수 search_lst에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인하여
True 또는 False를 담은 리스트 result를 반환하는 solution() 함수를 작성하세요.

[제약조건]
- lst의 노드는 정수로 이뤄져 있으며 1,000,000 개를 초과하지 않습니다.
- 이진 탐색 트리의 삽입과 탐색 기능을 구현해야 합니다.
- search_lst 의 길이는 10 이하 입니다.

[입출력 예]
lst                         search_lst          answer
[5, 3, 8, 4, 2, 1, 7, 10]   [1, 2, 5, 6]        [True, True, True, False]
[1, 3, 5, 7, 9]             [2, 4, 6, 8, 10]    [False, False, False, False, False]
'''
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BSTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        return
                    else:
                        current = current.right
    
    def search(self, data):
        current = self.root

        while current and current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        return current

def solution(lst, search_lst):
    bstree = BSTree()
    for data in lst:
        bstree.insert(data)
    
    result = []
    for search_data in search_lst:
        if bstree.search(search_data):
            result.append(True)
        else:
            result.append(False)
    
    return result

print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))
