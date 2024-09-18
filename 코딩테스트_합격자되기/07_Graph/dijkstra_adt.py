'''
다익스트라(Dijkstra) 알고리즘
- 양의 가중치가 있는 그래프의 최단 경로를 구하는 문제에서 활용도가 높음

    1. 시작 노드를 설정하고 시작 노드에서 모든 다른 노드들까지의 거리를 무한대로 초기화합니다.
    2. 시작 노드의 거리를 0으로 설정합니다.
    3. 방문하지 않은 노드 중 거리가 가장 작은 노드를 선택합니다. 처음에는 시작 노드가 선택됩니다.
    4. 선택된 노드의 인접한 노드들에 대해 현재의 거리보다 새로 계산된 거리
       (선택된 노드까지의 거리 + 인접한 노드와의 가중치)가 더 작은 경우, 거리 값을 업데이트합니다.
    5. 모든 인접한 노드들에 대해 거리가 업데이트되면, 해당 노드를 방문한 것으로 표시합니다.
    6. 모든 노드를 방문할 때까지 단계 3부터 5를 반복합니다.

[참조] : https://wing-beat.tistory.com/m/136


파이썬에서 heapq 모듈 사용
- 힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전 이진트리
- 힙의 속성: A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립

최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공
모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리(binary tree) 구조
내부적으로는 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소들(2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬됨

- heapq.heappush(heap, item) : item을 heap에 추가
- heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴하며, 비어 있는 경우 IndexError가 호출됨.
- heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N))

[참조] : https://littlefoxdiary.tistory.com/3
'''
import heapq

def dijkstra(graph, start):
    
    # 모든 노드의 거리값을 양의 무한대로 초기화
    distances = { node: float("inf") for node in graph }
    # print(distances)    # {'A': inf, 'B': inf, 'C': inf}

    # 시작 노드의 거리값을 0으로 초기화
    distances[start] = 0

    queue = []

    # 시작 노드를 큐에 삽입
    heapq.heappush(queue, [distances[start], start])

    # 시작 노드의 경로를 초기화
    paths = {start: [start]}

    ########## 이 부분 채워나가야 함 ##########

    sorted_paths = { node: paths[node] for node in sorted(paths) }

    return [distances, sorted_paths]


graph1 = {
    'A': {'B': 9, 'C': 3},
    'B': {'A': 5},
    'C': {'B': 1}
}

graph2 = {
    'A': {'B': 1},
    'B': {'C': 5},
    'C': {'D': 1},
    'D': {}
}

print(dijkstra(graph1, 'A'))
# [
#   { 'A': 0 ,'B': 4, 'C': 3 },
#   { 'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C'] }
# ]

print(dijkstra(graph2, 'A'))
# [
#   { 'A': 0 ,'B': 1, 'C': 6, 'D': 7 },
#   { 'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D'] }
# ]