'''
[문제 005] - https://school.programmers.co.kr/learn/courses/30/lessons/12949
2차원 행렬 arr1 과 arr2 를 입력받아 arr1 에 arr2 를 곱한 결과를 반환하는 solution() 함수를 완성하세요.

[제약조건]
- 행렬 arr1, arr2 의 행과 열의 길이는 2 이상 100 이하 입니다.
- 행렬 arr1, arr2 의 데이터는 -10 이상 20 이하인 자연수 입니다.
- 곱할 수 있는 배열만 주어집니다.

[입출력 예]
arr1                                arr2                                    return
[[1, 4], [3, 2], [4, 1]]            [[3, 3], [3, 3]]                        [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]   [[5, 4, 3], [2, 4, 1], [3, 1, 1]]       [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''
data = [
    {
        "arr1": [[1, 4], [3, 2], [4, 1]],
        "arr2": [[3, 3], [3, 3]]
    },
    {
        "arr1": [[2, 3, 2], [4, 2, 4], [3, 1, 4]],
        "arr2": [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    }
]

def solution_me(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            left = arr1[i]
            right = [arr2[k][j] for k in range(len(arr2))]
            data = 0
            for x in range(len(left)):
                data += left[x] * right[x]
            tmp.append(data)
        result.append(tmp)
    return result

def solution(arr1, arr2):
    row1, col1 = len(arr1), len(arr1[0])
    row2, col2 = len(arr2), len(arr2[0])

    result = [[0]*col2 for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result

for i in data:
    print(solution(i['arr1'], i['arr2']))
