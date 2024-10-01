'''
[문제 040]
주어진 그래프와 시작 노드를 이용하여 다익스트라 알고리즘을 구현하는 solution() 함수를 작성하세요.
인수는 graph, start 총 2개입니다.
graph는 딕셔너리로 주어지며, 노드의 연결 정보와 가중치가 저장되어 있습니다.
예를 들어, {'A': {'B': 2, 'C': 5}} 이면, A 는 B, C 에 각각 가중치 2, 5 로 연결되어 있는 것입니다.
start 는 문자열로 주어지며, 출발 노드를 의미합니다.
반환값은 시작노드부터 각 노드까지 최소 비용과 최단 경로를 포함한 리스트입니다.

[제약조건]
- 그래프의 노드 개수는 최대 10,000 개 입니다.
- 각 노드는 0 이상의 정수로 표현합니다.
- 모든 가중치는 0 이상의 정수이며 10,000 을 넘지 않습니다.

[입출력 예]
graph                           start           return
{                               'A'             [
    'A': {'B': 9, 'C': 3},                          {'A': 0, 'B': 4, 'C': 3},
    'B': {'A': 5},                                  {
    'C': {'B': 1}                                       'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']
}                                                   }
                                                ]
{                               'A'             [
    'A': {'B': 1},                                  {'A': 0, 'B': 4, 'C': 3},
    'B': {'C': 5},                                  {
    'C': {'D': 1},                                      'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D']
    'D': { }                                        }
}                                               ]
'''
import heapq

def solution(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    paths = {start: [start]}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight

            if distances[adjacent_node] > distance:
                distances[adjacent_node] = distance
                paths[adjacent_node] = paths[current_node] + [adjacent_node]

                heapq.heappush(queue, [distance, adjacent_node])
    
    sorted_paths = {node: paths[node] for node in sorted(paths)}

    return [distances, sorted_paths]

print(solution(
    {'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1}},
    'A'
))
