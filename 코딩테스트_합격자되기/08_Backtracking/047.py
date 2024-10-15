'''
[문제 047]
정수 N을 입력받아 1부터 N까지의 숫자 중에서 합이 10이 되는 조합을 리스트로 반환하는 solution() 함수를 작성하세요.

[제약조건]
- 백트래킹을 활용해야 합니다.
- 숫자 조합은 오름차순으로 정렬되어야 합니다.
- 같은 숫자는 한 번만 선택할 수 있습니다.
- N은 1 이상 10 이하인 정수입니다.

[입출력 예]
N           result
5           [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
2           []
7           [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [3, 7], [4, 6]]
'''
def solution(N):
    result = []

    def back_tracker(sum, selected_nums, start):
        if sum == 10:
            result.append(selected_nums)
            return
        
        for i in range(start, N+1):
            if sum+i <= 10:
                back_tracker(sum+i, selected_nums+[i], i+1)
    
    back_tracker(0, [], 1)
    return result

print(solution(5))