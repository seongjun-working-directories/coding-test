'''
[문제 046] - https://programmers.co.kr/learn/courses/30/lessons/86971
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다.
당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다.
이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다.
전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때,
두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

[제약조건]
- n은 2 이상 100 이하인 자연수입니다.
- wires는 길이가 n-1인 정수형 2차원 배열입니다.
    - wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
    - 1 ≤ v1 < v2 ≤ n 입니다.
    - 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

[입출력 예]
n	wires	                                            result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	                                0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	            1
'''
from collections import defaultdict
from copy import deepcopy

def my_tree_builder(wires):
    tree = defaultdict(list)
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
    return tree

def solution_me(n, wires):
    answer = n
    for i in range(len(wires)):
        tmp_wires = deepcopy(wires)
        tmp_wires.pop(i)
        tree = my_tree_builder(tmp_wires)
        
        key = list(tree.keys())[0]
        
        visited = set()
        queue = [key]
        while queue:
            element = queue.pop(0)
            visited.add(element)
            
            for k in tree[element]:
                if k not in visited:
                    queue.append(k)
        
        set_1 = len(list(visited))
        set_2 = n - set_1
        answer = min(answer, abs(set_1-set_2))
        
    return answer

# ==============================================================

def tree_builder(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def dfs(graph, node, parent):
    cnt = 1
    for child in graph[node]:
        if child != parent:
            cnt += dfs(graph, child, node)
    return cnt

def solution(n, wires):
    graph = tree_builder(n, wires)
    
    min_diff = float("inf")
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnt_a = dfs(graph, a, b)
        cnt_b = n - cnt_a
        
        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return min_diff


print(solution_me(
    9,
    [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
))

print(solution(
    9,
    [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
))