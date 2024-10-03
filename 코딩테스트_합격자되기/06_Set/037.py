'''
[문제 037] - https://school.programmers.co.kr/learn/courses/30/lessons/42861
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한
최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다.
예를 들어 A 섬과 B 섬 사이에 다리가 있고,
B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

[제약조건]
- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 ((n-1) * n) / 2이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고,
  costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다.
  즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다.

[입출력 예]
n	costs	                                    return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
'''
def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def solution(n, costs):
    '''
    - 각 섬 사이의 다리를 건설하는 비용을 오름차순으로 정렬
    - 비용이 작은 다리부터 선택해 섬을 연결
    - N 개의 섬을 연결하려면, N-1 개의 다리가 필요하므로 N-1 개의 다리가 선택될 때까지 위 두 과정을 반복
    - 비용을 최소화하기 위해 다리를 추가할 때 사이클이 생기지 않도록 해야 함
    - 사이클 여부는 다리를 추가할 때 다리에 연결될 섬들의 루트노드가 같은지 확인하므로써 검사 가능    
    '''
    # 가중치를 기준으로 간선을 오름차순 정렬
    # 이를 통해 굳이 가중치를 매번 비교하지 않더라도
    # 이미 연결된 간선이 새로 연결하려는 간선보다 낮은 가중치를 가진다는 걸 보장할 수 있음
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    rank = [0] * n
    
    # 최소 신장 트리의 총 비용와 총 간선 수를 초기화
    min_cost = 0
    edges = 0
    
    for edge in costs:
        if edges == (n-1):
            break
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1
    
    return min_cost

print(solution(
    4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
))