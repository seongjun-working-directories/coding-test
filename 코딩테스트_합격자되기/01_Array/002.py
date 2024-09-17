'''
[문제 002]
정수 배열을 하나 받습니다.
배열의 중복값을 제거하고 배열 데이터를 내림차순으로 정렬해서 반환하는 solution() 함수를 완성하세요.

[제약조건]
- 배열 길이는 2 이상 1,000 이하 입니다.
- 각 배열의 데이터 값은 -100,000 이상 100,000 이하 입니다.

[입출력 예]
입력                    출력
[4, 2, 2, 1, 3, 4]      [4, 3, 2, 1]
[2, 1, 1, 3, 2, 5, 4]   [5, 4, 3, 2, 1]
'''
data = [
    [4, 2, 2, 1, 3, 4],
    [2, 1, 1, 3, 2, 5, 4]
]

def solution(arr):
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    return unique_arr
    
for i in data:
    print(solution(i))
