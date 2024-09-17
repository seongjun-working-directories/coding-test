'''
[문제 026]
이진 트리를 표현한 리스트 nodes를 인자로 받습니다.
예를 들어서 nodes가 [1, 2, 3, ..., 7] 이면, 다음과 같은 트리를 표현한 것입니다.

                1
        2               3
    4       5       6       7

해당 이진트리에 대해 전위 순회, 중위 순회, 후위 순회 결과를 반환하는 solution() 함수를 작성하세요.

[제약조건]
- 입력 노드값의 개수는 1개 이상 1,000개 이하 입니다.
- 노드값은 정수형이며, 중복되지 않습니다.

[입출력 예]
nodes                       return
[1, 2, 3, 4, 5, 6, 7]       ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]
'''
def preorder(nodes, index):
    # index가 노드 리스트의 길이보다 작을때
    if index < len(nodes):
        # 루트 노드 우선 출력
        # 이후, 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출하여 출력 순서대로 이어붙임
        ret = str(nodes[index]) + " "
        ret += preorder(nodes, index * 2 + 1)
        ret += preorder(nodes, index * 2 + 2)
        return ret
    
    # index >= len(nodes)일 때는 빈 문자열 반환
    else:
        return ""

def inorder(nodes, index):
    if index < len(nodes):
        ret = inorder(nodes, index * 2 + 1)
        ret += str(nodes[index]) + " "
        ret += inorder(nodes, index * 2 + 2)
        return ret
    
    else:
        return ""

def postorder(nodes, index):
    if index < len(nodes):
        ret = postorder(nodes, index * 2 + 1)
        ret += postorder(nodes, index * 2 + 2)
        ret += str(nodes[index]) + " "
        return ret
    
    else:
        return ""

def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],    # 마지막 공백 제거
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]
    ]

print(solution([1, 2, 3, 4, 5, 6, 7]))
