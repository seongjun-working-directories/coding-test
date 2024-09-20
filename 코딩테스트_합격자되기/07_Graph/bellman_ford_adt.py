'''
벨만-포드 알고리즘(Bellman-Ford Algorithm)
- 다익스트라 알고리즘과 마찬가지로 노드에서 노드까지의 최소 비용을 구함
- 대신 벨만-포드 알고리즘은 매 단계마다 모든 간선의 가중치를 재확인하여 최소 비용을 갱신함
- 즉, 벨만-포드 알고리즘은 음수 가중치에 대한 대응이 가능

    1. 시작 노드 설정 후 다음 시작 노드의 최소 비용은 0, 나머지 노드는 INF로 초기화
        => 이후 최소 비용을 갱신할 때 직전 노드도 갱신
    2. 노드 개수 -1 만큼 다음 연산을 반복
        2-1. 시작 노드에서 갈 수 있는 각 노드에 대하여 "전체 노드 각각을 거쳐갈 때
             현재까지 구한 최소비용보다 더 적은 최소 비용이 있는지 확인"하여 갱신
              => 최소 비용 갱신 시, V의 직전 노드 값도 함께 갱신
    3. 과정 2를 마지막으로 한번 더 수행하여 갱신되는 최소 비용이 있는지 확인
        => 만약, 있는 경우 음의 순환이 있음을 의미 
'''
def bellman_ford(graph, sources):
    # 그래프의 노드 수
    num_vertices = len(graph)
    
    # 거리 배열 초기화
    distance = [ float("inf") ] * num_vertices
    distance[sources] = 0

    # 직전 경로 배열 초기화
    predecessor = [None] * num_vertices

    # 간선 수 만큼 반복하여 최단 경로 갱신
    for temp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                # 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가
                # 기존에 저장된 노드 v까지의 거리보다 짧은 경우
                if distance[u] + weight < distance[v]:
                    # 최단 거리 갱신
                    distance[v] = distance[u] + weight
                    # 직전 경로 갱신
                    predecessor[v] = u
    
    # 음의 가중치를 순회하며 확인
    for u in range(num_vertices):
        for v, weight in graph[u]:
            # 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가
            # 기존에 저장된 노드 v까지의 거리보다 짧은 경우
            if distance[u] + weight < distance[v]:
                # 음의 가중치 순회 발견 -> [-1] 반환
                return [-1]
    
    return [distance, predecessor]


graph1 = [
    [(1, 4), (2, 3), (4, -6)],
    [(3, 5)],
    [(1, 2)],
    [(0, 7), (2, 4)],
    [(2, 2)]
]

graph2 = [
    [(1, 5), (2, -1)],
    [(2, 2)],
    [(3, -2)],
    [(0, 2), (1, 6)]
]

print(bellman_ford(graph1, 0))
# [
#   [0, -2, -4, 3, -6],
#   [None, 2, 4, 1, 0]
# ]

print(bellman_ford(graph2, 0))
# [
#   -1
# ]
