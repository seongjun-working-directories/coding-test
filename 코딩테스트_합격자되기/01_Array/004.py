'''
[문제 004] - https://programmers.co.kr/learn/courses/30/lessons/42840
수포자는 수학을 포기한 사람을 줄인 표현입니다.
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

- 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, ...
- 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
- 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answers 가 주어졌을 때
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환하도록 solution() 함수를 작성하세요.

[제약조건]
- 시험은 최대 10,000 문제로 구성되어 있습니다.
- 문제의 정답은 1, 2, 3, 4, 5 중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿이라면 반환하는 값을 오름차순으로 정렬하세요.

[입출력 예]
answers             return
[1, 2, 3, 4, 5]     [1]
[1, 3, 2, 4, 2]     [1, 2, 3]
'''
data = [
    [1, 2, 3, 4, 5],
    [1, 3, 2, 4, 2]
]

def solution_me(arr):
    a_way = [1, 2, 3, 4, 5]
    b_way = [2, 1, 2, 3, 2, 4, 2, 5]
    c_way = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    counter = [0, 0, 0]  # 순서대로 a_way, b_way, c_way 정답 개수
    
    for i in range(len(arr)):
        if a_way[i%len(a_way)] == arr[i]:
            counter[0] += 1
        if b_way[i%len(b_way)] == arr[i]:
            counter[1] += 1    
        if c_way[i%len(c_way)] == arr[i]:
            counter[2] += 1
    
    top_ranker = []
    for i in range(len(counter)):
        if (counter[i] == max(counter)):
            top_ranker.append(i+1)
    
    return top_ranker

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0]*3
    
    # >>> print( list(enumerate(['eat', 'sleep', 'repeat'])) )
    # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores[j] += 1
    
    max_score = max(scores)
    
    highest_scores = []
    for i, scores in enumerate(scores):
        if scores == max_score:
            highest_scores.append(i+1)
    
    return highest_scores

for i in data:
    print(solution(i))
