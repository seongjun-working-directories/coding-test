'''
[문제 039]
너비 우선 탐색으로 모든 노드를 순회하는 함수 solution()을 작성하세요.
시작노드는 start로 주어집니다.
graph는 (출발노드, 도착노드) 쌍들이 들어있는 리스트입니다.
반환값은 그래프의 시작노드부터 모든 노드를 너비 우선 탐색으로 진행한 순서대로 노드가 저장된 리스트입니다.

[제약조건]
- 노드의 최대 개수는 100개를 넘지 않습니다.
- 시작노드부터 시작해서 모든 노드를 방문할 수 있는 경로가 항상 있습니다.
- 그래프의 노드는 숫자입니다.

[입출력 예]
graph                                                                               start       return
[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]    1           [1, 2, 3, 4, 5, 6, 7, 8, 9]
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]                                    1           [1, 2, 3, 4, 5, 0]
'''
from collections import defaultdict, deque

# 1. 입력값을 인접리스트 형태로 변환
def graph_to_adjacent_list(graph):
    adjacent_list = defaultdict(list)
    for u, v in graph:
        adjacent_list[u].append(v)
    return adjacent_list

# 2. BFS 알고리즘을 사용
def bfs(adjacent_list, start, visited, result):
    queue = deque([start])
    visited.add(start)
    result.append(start)

    while queue:
        node = queue.popleft()
        
        for neighbor in adjacent_list[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                result.append(neighbor)

# 3. 실행
def solution(graph, start):
    adjacent_list = graph_to_adjacent_list(graph)
    # print(adjacent_list)

    visited = set()
    result = []
    bfs(adjacent_list, start, visited, result)

    return result

print(solution(
    [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],
    1
))