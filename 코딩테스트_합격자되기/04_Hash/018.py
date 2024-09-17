'''
[문제 018]
n개의 양의 정수로 이뤄진 리스트 arr와 정수 target이 주어졌을때,
이 중에서 합이 target인 두 수가 arr에 있는지 찾고,
있으면 True, 없으면 False를 반환하는 solution() 함수를 작성하세요.

[제약조건]
- n은 2 이상 10,000 이하의 자연수입니다.
- arr의 각 원소는 1 이상 10,000 이하의 자연수입니다.
- arr의 원소 중 중복되는 원소는 없습니다.
- target은 1 이상 20,000 이하의 자연수입니다.

[입출력 예]
arr                 target      return
[1, 2, 3, 4, 8]     6           True
[2, 3, 5, 9]        10          False
'''
def count_sort(arr, k):
    hash_table = [0] * (k+1)

    for num in arr:
        if num <= k:
            hash_table[num] = 1
    
    return hash_table

def solution(arr, target):
    hash_table = count_sort(arr, target)

    print(hash_table)

    for num in arr:
        complement = target - num

        if (
            complement != num
            and complement >= 0
            and complement <= target
            and hash_table[complement] == 1
        ):
            return True

    return False

print(solution([1, 2, 3, 4, 8], 6))