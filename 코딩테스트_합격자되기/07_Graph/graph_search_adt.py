'''
[참조]: https://wikidocs.net/196183, https://wikidocs.net/196284

그래프 탐색

1. 깊이 우선 탐색(DFS)

시작 노드부터 탐색을 시작하여 간선을 따라 최대 깊이 노드까지 이동하며 차례로 방문
최대 깊이 노드까지 방문한 다음 이전에 방문한 노드를 거슬러 올라가며
해당 노드와 연결된 노드 중 방문하지 않은 노드로 다시 최대 깊이까지 차례로 방문

    - a. 시작 노드 결정 후 스택에 시작 노드를 푸쉬
        => 스택에 있는 노드는 방문 예정인 노드를 의미
    - b. 스택이 비었는지 확인
        => 스택이 비었다면, 더 이상 갈 노드가 없는 것이므로 탐색을 종료
    - c. 스택에서 노드를 팝함
        => 팝한 원소는 최근에 스택에 푸쉬한 노드임
    - d. 팝한 노드의 방문 여부를 확인하고 아직 방문하지 않았다면 노드를 방문 처리
    - e. 방문한 노드와 인접한 모든 노드를 확인하고 그 중 방문하지 않은 노드를 스택에 푸쉬
        => 스택은 FILO 구조이므로, 방문 순서를 오름차순으로 고려한다면 역순으로 노드를 푸쉬

고려할 사항은 다음과 같음
- 탐색할 노드가 없을 때까지 간선을 타고 내려갈 수 있어야 함
- 가장 최근에 방문한 노드를 알 수 있어야 함
- 이미 방문한 노드인지 확인할 수 있어야 함
'''

graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} # 무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 # 방향 그래프

def DFS_STACK(graph, node):
    result = []

    # 방문할 노드를 저장하는 스택으로 시작노드를 기본적으로 넣어놓고 시작
    stack = [node]

    # 방문 여부를 확인한 집합을 만듦
    visited = set(stack)

    # 스택이 빌 때까지 반복
    while stack:
        top = stack.pop()
        result.append(top)

        # 현재 노드에 연결된 다른 노드를 확인
        # 다른 노드가 아직 방문하지 않은 노드라면, 스택과 집합에 넣음
        for element in graph[top]:
            if element not in visited:
                visited.add(element)
                stack.append(element)
    
    return result

print("무방향 그래프의 깊이 우선 탐색")
print("=================================")
print("노드 1에서 시작: ", DFS_STACK(graph1, 1))
print("노드 2에서 시작: ", DFS_STACK(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("=================================")
print("노드 1에서 시작: ", DFS_STACK(graph2, 1))
print("노드 2에서 시작: ", DFS_STACK(graph2, 5))
print()


def DFS_RECURSIVE(graph, node):
    result = []
    visited = set()

    # 인수로 들어온 노드를 방문 처리하고,
    # 아직 방문하지 않은 노드를 탐색하는 재귀함수
    def _dfs_recursive(top):
        # 이미 방문한 노드이면 종료
        if top in visited:
            return

        # 현재 노드를 방문 처리
        visited.add(top)
        result.append(top)

        # 현재 노드와 간선으로 연결된 노드들을 깊이 우선 탐색함
        for element in graph[top]:
            _dfs_recursive(element)
    
    _dfs_recursive(node)
    return result

print("무방향 그래프의 깊이 우선 탐색")
print("=================================")
print("노드 1에서 시작: ", DFS_STACK(graph1, 1))
print("노드 2에서 시작: ", DFS_STACK(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("=================================")
print("노드 1에서 시작: ", DFS_STACK(graph2, 1))
print("노드 2에서 시작: ", DFS_STACK(graph2, 5))
print()

'''
2. 너비 우선 탐색(BFS)

시작 노드와 거리가 가장 가까운 노드를 우선하여 방문하는 알고리즘
즉, 시작 노드와 목표 노드까지의 차수가 같은 것을 우선적으로 방문
단, 간선 가중치의 합이 아님에 주의

탐색 시, 시작 노드를 정하고 큐(Queue)에 시작 노드를 푸쉬
시작 노드를 큐에 푸쉬하면서 방문 처리함
즉, 큐에 있는 노드는 "이미 방문 처리"되었으며, 그 노드와 "인접한 노드는 아직 탐색하지 않은 상태"
이후 다음의 과정을 반복

    - a. 큐가 비었는지 확인
        => 큐가 비었다면, 모든 노드를 방문했음을 의미하므로 탐색을 종료
    - b. 큐에서 노드를 꺼냄
    - c. 꺼낸 노드와 인접한 모든 노드를 확인하고 그 중 아직 방문하지 않은 노드를 큐에 푸쉬하며 방문 처리

고려할 사항은 다음과 같음
- 현재 방문한 노드와 직접 연결된 모든 노드를 방문할 수 있어야 함
- 이미 방문한 노드인지 확인할 수 있어야 함
'''
from collections import deque

graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} # 무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 # 방향 그래프

def BFS_QUEUE(graph, node):
    result = []

    queue = deque()
    queue.append(node)
    visited = set(queue)

    while queue:
        u = queue.popleft()
        result.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

    return result

print("무방향 그래프의 너비 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", BFS_QUEUE(graph1, 1))
print("노드 2에서 시작: ", BFS_QUEUE(graph1, 2))
print()
print("방향 그래프의 너비 우선 탐색")
print("========================")
print("노드 1에서 시작: ", BFS_QUEUE(graph2, 1))
print("노드 2에서 시작: ", BFS_QUEUE(graph2, 2))
print()

'''
깊이 우선 탐색
(1) 가장 깊은 곳을 우선 탐색하고, 더 이상 탐색할 수 없으면 백트래킹하여 최근 방문 노드부터 다시 탐색
(2) "모든 가능한 해"를 찾는 백트래킹 알고리즘 구현에 사용 가능
(3) "그래프의 사이클"을 감지하는 경우 사용 가능
(4) 최단 경로를 제외한 탐색에서, 깊이 우선 탐색을 우선 고려해야 함

너비 우선 탐색
(1) 찾은 노드가 시작 노드로부터 최단 경로임을 보장
(2) 미로 찾기 문제에서 최단 경로를 찾거나, 네트워크 분석 문제를 풀 때 사용 가능
'''