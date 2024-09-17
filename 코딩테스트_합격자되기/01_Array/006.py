'''
[문제 006] - https://school.programmers.co.kr/learn/courses/30/lessons/42889
오렐리를 위해 실패율을 구한느 코드를 완성하세요.
- 실패율 정의 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

전체 스테이지 개수가 N, 게임을 이용하는 사용자가 현재 멈춰 있는 스테이지의 번호가 담긴 배열 stages가 주어질 때
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 반환하도록 solution() 함수를 완성하세요.

[제약조건]
- 스테이지 개수 N은 1 이상 500 이하 자연수입니다.
- stages의 길이는 1 이상 200,000 이하 입니다.
- stages에는 1 이상 N + 1 이하의 자연수가 담겨있습니다.
    - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타냅니다.
    - 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타냅니다.
- 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 됩니다.
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의합니다.

[입출력 예]
N   stages                      result
5   [2, 1, 2, 6, 2, 4, 3, 3]    [3, 4, 2, 1, 5]
4   [4, 4, 4, 4, 4]             [4, 1, 2, 3]

입출력 예 #1
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.
1 번 스테이지 실패율 : 1/8

2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.
2 번 스테이지 실패율 : 3/7

마찬가지로 나머지 스테이지의 실패율은 다음과 같다.
3 번 스테이지 실패율 : 2/4
4번 스테이지 실패율 : 1/2
5번 스테이지 실패율 : 0/1

각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.
[3,4,2,1,5]

입출력 예 #2
모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.
[4,1,2,3]
'''
def solution_me(N, stages):
    counter = list(enumerate([0]*N, 1))

    stages.sort()

    for i in range(len(counter)):
        try:
            up = stages.count(i+1)
            down = len(stages) - stages.index(i+1)
            counter[i] = (i+1, up/down)
        except:
            counter[i] = (i+1, 0)
    
    counter.sort(key=lambda x: x[1], reverse=True)

    return [counter[i][0] for i in range(len(counter))]

def solution(N, stages):
    challenger = [0]*(N+2)
    for stage in stages:
        challenger[stage] += 1
    
    fails = {}
    total = len(stages)

    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i]/total
            total -= challenger[i]
    
    result = sorted(fails, key=lambda x:fails[x], reverse=True)
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
