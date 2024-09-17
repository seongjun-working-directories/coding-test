'''
[문제 003] - https://programmers.co.kr/learn/courses/30/lessons/68644
정수 배열 numbers 가 주어집니다.
numbers 에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에
오름차순으로 담아 반환하는 solution() 함수를 완성하세요.

[제약조건]
- numbers 의 길이는 2 이상 100 이하 입니다.
- numbers 의 모든 수는 0 이상 100 이하 입니다.

[입출력 예]
numbers             result
[2, 1, 3, 4, 1]     [2, 3, 4, 5, 6, 7]
[5, 0, 2, 7]        [2, 5, 7, 9, 12]
'''
data = [
    [2, 1, 3, 4, 1],
    [5, 0, 2, 7]
]

def solution(arr):
    add_result = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            add_result.append(arr[i] + arr[j])
    result = list(set(add_result))
    result.sort()
    return result

for i in data:
    print(solution(i))
