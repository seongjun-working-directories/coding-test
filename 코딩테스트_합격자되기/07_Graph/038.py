'''
[문제 038]
깊이 우선 탐색으로 모든 그래프의 노드를 순회하는 함수 solution()을 작성하세요.
시작노드는 start로 주어집니다.
graph는 [출발노드, 도착노드] 쌍들이 들어있는 리스트입니다.
반환값은 그래프의 시작노드부터 모든 노드를 깊이 우선 탐색으로 진행한 순서대로 노드가 저장된 리스트입니다.

[제약조건]
- 노드의 최대 개수는 100개를 넘지 않습니다.
- 시작노드부터 시작해서 모든 노드를 방문할 수 있는 경로가 항상 있습니다.
- 그래프의 노드는 문자열입니다.

[입출력 예]
graph                                                                       start       return
[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]                            'A'         ['A', 'B', 'C', 'D', 'E']    
[['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]    'A'         ['A', 'B', 'D', 'E', 'F', 'C']
'''
from collections import defaultdict

# 1. 입력값을 인접리스트 형태로 변환
def graph_to_adjacent_list(graph):
    adjacent_list = defaultdict(list)
    for u, v in graph:
        adjacent_list[u].append(v)
    return adjacent_list

# 2. DFS 알고리즘을 사용
def dfs(adjacent_list, node, visited, result):
    visited.add(node)
    result.append(node)

    for neighbor in adjacent_list[node]:
        if neighbor not in visited:
            dfs(adjacent_list, neighbor, visited, result)

# 3. 실행
def solution(graph, start):
    adjacent_list = graph_to_adjacent_list(graph)
    # print(adjacent_list)

    visited = set()
    result = []
    dfs(adjacent_list, start, visited, result)
    
    return result

print(solution(
    [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']],
    'A'
))
