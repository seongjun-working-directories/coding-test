'''
[문제 041]
벨만-포드 알고리즘을 구현한 solution() 함수를 구현하세요.
graph의 각 데이터는 리스트입니다.
첫 번째 데이터는 0번 노드 기준으로 연결된 노드 정보, 두 번째 데이터는 1번 노드 기준으로 연결된 노드 정보입니다.
노드 정보의 구성은 (노드, 가중치)와 같습니다. source는 시작 노드입니다.
반환값은 최단 거리를 담은 distance 리스트와 최단 거리와 함께 관리할 직전 노드 predecessor를 리스트에 차례로 담아서
[distance, predecessor] 형식으로 반환하면 됩니다.
predecessor에서 시작 노드는 None으로 표시합니다.
만약 음의 가중치 순회가 있다면, [-1]을 반환하세요.
음의 가중치 순회란 순환하면 할수록 가중치의 합이 적어지는 순회를 말합니다.

[제약조건]
- 노드의 최대 개수는 100 개 입니다.
- 각 간선의 가중치는 -100 이상 100 이하입니다.

[입출력 예]
graph                               source      return
[                                   0           [
    [(1, 4), (2, 3), (4, -6)],                      [0, -2, -4, 3, -6],
    [(3, 5)],                                       [None, 2, 4, 1, 0]
    [(1, 2)],                                   ]
    [(0, 7), (2, 4)],
    [(2, 2)]
]
[                                   0           [-1]
    [(1, 5), (2, -1)],
    [(2, 2)],
    [(3, -2)],
    [(0, 2), (1, 6)]
]
'''
def solution(graph, source):
    # 그래프의 노드 수
    num_vertices = len(graph)

    distance = [float("inf")] * num_vertices
    distance[source] = 0

    # 직전 경로 배열 초기화
    predecessor = [None] * num_vertices

    for tmp in range(num_vertices-1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
    
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return [-1]

    return [distance, predecessor]

print(solution(
    [[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]],
    0
))
