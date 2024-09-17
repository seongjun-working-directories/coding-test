'''
배열로 이진 트리 표현하기
- 루트 노드는 배열 인덱스 1번에 저장합니다.
- 왼쪽 자식 노드의 배열 인덱스는 부모 노드의 배열 인덱스 X 2 입니다.
- 오른쪽 자식 노드의 배열 인덱스는 부모 노드의 배열 인덱스 X 2 + 1 입니다.

이진 트리 순회하기
- 전위 순회 : 현재 노드를 부모 노드로 생각했을 때, 부모 노드 -> 왼쪽 자식 노드 -> 오른쪽 자식 노드 순서로 방문
- 중위 순회 : 현재 노드를 부모 노드로 생각했을 때, 왼쪽 자식 노드 -> 부모 노드 -> 오른쪽 자식 노드 순서로 방문
- 후위 순회 : 현재 노드를 부모 노드로 생각했을 때, 왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 부모 노드 순서로 방문

* 중위 순회는 현재 노드를 거치기만 할 뿐 '방문'하지 않음

포인터로 트리를 표현하는 방법
- 
                            -----------------------------------------------
                            | 왼쪽 자식 노드 |   값   | 오른쪽 자식 노드 |
                            -----------------------------------------------
                            /                                              \
                           /                                                \
-----------------------------------------------        -----------------------------------------------
| 왼쪽 자식 노드 |   값   | 오른쪽 자식 노드 |         | 왼쪽 자식 노드 |   값   | 오른쪽 자식 노드 |
-----------------------------------------------        -----------------------------------------------

이진 탐색 트리 구축
- 찾으려는 값이 현재 노드의 값과 같으면 탐색을 종료
- 찾으려는 값이 현재 노드보다 크면 오른쪽 노드를 탐색
- 찾으려는 값이 현재 노드보다 작으면 왼쪽 노드를 탐색
- 노드가 없을 때까지 계속 탐색했는데 값이 없다면 현재 트리에 값이 없는 것

* 다만, 균형 이진 탐색 트리가 아닌 치우쳐진 형태의 트리는 배열만큼 효율이 낮아질 수 있음
* 참조 : https://wikidocs.net/195269, https://www.geeksforgeeks.org/introduction-to-avl-tree/
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    # __contains__ 메서드로 in 또는 not in을 사용할 수 있음
    def __contains__(self, data):
        node = self.root
        while node:
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right
        return False
    
    # 메서드를 제대로 만들었는지 확인하기 위해 중위 순회 메서드를 만듦
    def inorder(self):
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)
        res = []
        _inorder(self.root)
        return res
    
    # 현재 노드의 값과 삽입할 값을 비교하여 왼쪽이나 오른쪽 노드를 이동
    # 자식 노드가 비었는지를 매번 확인하지 말고, 빈 노드가 나올 때까지 계속 이동
    # 노드를 이동하기 전에 현재 노드를 임시 저장
    # 빈 노드가 나오면 임시 저장한 부모 노드의 값과 비교하여 왼쪽이나 오른쪽 노드에 값을 추가
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        node = self.root
        while node is not None:
            parent = node
            if node.data > data:
                node = node.left
            else:
                node = node.right
        if parent.data > data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
    
    def insert_recursive(self, data):
        def _insert(node, data):
            if node is None:
                return Node(data)
            
            if node.data > data:
                node.left = _insert(node.left, data)
            else:
                node.right = _insert(node.right, data)
            return node
        self.root = _insert(self.root, data)
    
    #삭제할 노드가 리프 노드이거나 자식이 하나일 때 처리한다.
    #왼쪽 자식이 있으면 반환하고, 그렇지 않으면 오른쪽 자식을 반환한다.
    #리프 노드이면 왼쪽과 오른쪽이 모두 None이므로, None을 반환한다.
    def _del_node1(self, del_node):
        if del_node.left:
            return del_node.left
        return del_node.right

    #자식이 둘인 노드를 삭제한다.
    def _del_node2(self, del_node):
        #삭제할 노드의 오른쪽에서 가장 왼쪽 노드와 부모 노드를 찾는다.
        parent = del_node
        leftmost = del_node.right
        while leftmost.left:
            parent = leftmost
            leftmost = leftmost.left

        #삭제 노드의 값을 가장 왼쪽 노드의 값으로 대체한다.
        del_node.data = leftmost.data

        #가장 왼쪽 노드를 삭제한다.
        #가장 왼쪽 노드는 리프 노드이거나 오른쪽에 자식이 있다.
        if del_node == parent:
            parent.right = self._del_node1(leftmost)
        else:
            parent.left = self._del_node1(leftmost)

    #삭제시 실제 사용할 메서드
    def delete(self, data):
        #루트가 None일 때와 삭제 대상일 때를 처리한다.
        if self.root is None:
            return
        if self.root.data == data:
            if self.root.left and self.root.right:
                self._del_node2(self.root)
            else:
                self.root = self._del_node1(self.root)
            return

        #삭제할 노드와 그 부모 노드를 찾는다.
        del_node = self.root
        while del_node and del_node.data != data:
            parent = del_node
            if del_node.data > data:
                del_node = del_node.left
            else:
                del_node = del_node.right

        #삭제할 노드가 없으면 종료
        if del_node is None: 
            return

        #삭제할 노드의 자식이 둘일 때
        if del_node.left and del_node.right:
            self._del_node2(del_node)
            return
        
        #삭제할 노드가 리프 노드이거나 자식이 하나일 때
        if parent.left == del_node:
            parent.left = self._del_node1(del_node)
        else:
            parent.right = self._del_node1(del_node)

# TEST CODE
#                       6
#           4                       9
#   2               5       7
#                               8

binary_search_tree = Binary_Search_Tree()
binary_search_tree.root = Node(6)
binary_search_tree.root.left = Node(4)
binary_search_tree.root.right = Node(9)
binary_search_tree.root.left.left = Node(2)
binary_search_tree.root.left.right = Node(5)
binary_search_tree.root.right.left = Node(7)
binary_search_tree.root.right.left.right = Node(8)

print(f"Inorder traversal: {binary_search_tree.inorder()}")
# Inorder traversal: [2, 4, 5, 6, 7, 8, 9]

for x in (2, 3, 6, 9):
    if x in binary_search_tree:
        print(f"{x} is found.")
    else:
        print(f"{x} is not found.")

binary_search_tree.insert(1)
binary_search_tree.insert(15)
binary_search_tree.insert(11)

print(f"Inorder traversal: {binary_search_tree.inorder()}")
# Inorder traversal: [1, 2, 4, 5, 6, 7, 8, 9, 11, 15]

binary_search_tree.delete(5)
print(f"5를 삭제 후: {binary_search_tree.inorder()}")