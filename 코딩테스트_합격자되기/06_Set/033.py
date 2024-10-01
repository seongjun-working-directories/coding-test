'''
[문제 033]
상호배타적 집합을 표현하고 관리하는데 다음 두 연산이 필요합니다.
- union(x, y): x와 y가 속한 두 집합을 합칩니다.
- find(x): x가 속한 집합의 대표 원소(루트노드)를 찾습니다.

operations라는 배열은 수행할 연산을 의미합니다. 연산 종류는 2개입니다.
- ['u', 1, 2]는 노드 1과 노드 2에 대해 union 연산 수행
- ['f', 3]은 3의 루트 노드를 찾기 위해 find 연산 수행

초기의 노드는 부모 노드를 자신의 값으로 설정했다고 가정하며,
각 집합의 루트노드를 기준으로 루트노드가 작은 노드를 더 큰 노드의 자식으로 연결하는 방법을 사용합니다.
operations에 있는 연산을 모두 수행한 후 집합의 개수를 반환하는 solution() 함수를 구현해주세요.

[제약조건]
- 0 <= k <= 1000 : 노드의 개수
- 1 <= len(operations) <= 100000
- operations[i][0]은 문자열 'u', 'f' 중 하나
- 'u'는 union 연산, union 연산 뒤로는 두 개의 정수 x, y가 나옴
- 'f'는 find 연산, find 연산 뒤로는 하나의 정수 x가 나옴
- x와 y는 0 이상 k-1 이하의 정수
- 연산은 항상 유효함(즉, union과 find의 인수는 상호배타적 집합 내에 있는 노드번호)

[입출력 예]
k       operations                              result
3       [['u', 0, 1], ['u', 1, 2], ['f', 2]]    1
4       [['u', 0, 1], ['u', 2, 3], ['f', 0]]    2
'''
def find(parents, x):
    if parents[x] == x:
        return parents[x]

    parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    root1 = find(parents, x)
    root2 = find(parents, y)

    parents[root2] = root1

def solution(k, operations):
    parents = [i for i in range(k)]

    for operation in operations:
        if operation[0] == 'u':
            union(parents, operation[1], operation[2])
        else:
            find(parents, operation[1])
    
    n = len(set(find(parents, i) for i in range(k)))
    return n

print(solution(3, [['u', 0, 1], ['u', 1, 2], ['f', 2]]))
print(solution(4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]))
