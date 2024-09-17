'''
[문제 019]
문자열 리스트 string_list와 쿼리 리스트 query_list가 있을 때,
각 쿼리 리스트에 있는 문자열이 string_list의 문자열 리스트에 있는지 여부를 확인해야 합니다.
문자열이 있으면 True, 없으면 False가 됩니다.
각 문자열에 대해서 문자열의 존재 여부를 리스트 형태로 반환하는 solution() 함수를 작성하세요.

[제약조건]
- 입력 문자열은 영어 소문자로만 이뤄져 있습니다.
- 문자열의 최대 길이는 10^6 입니다.
- 해시 충돌은 없습니다.
- 아래와 같은 문자열 해싱 방법을 활용해서 해싱 함수를 구현하세요.
- 다음 식에서 p는 31, m(=버킷크기)은 1,000,000,007 로 합니다.
  - hash(s) = (s[0] + s[1]*p + s[2]*p^2 + ... + s[n-1]*p^(n-1)) mod m

[입출력 예]
string_list                     query_list                              return
["apple", "banana", "cherry"]   ["banana", "kiwi", "melon", "apple"]    [True, False, False, True]
'''
def polynomial_hash(str):
    p = 31
    m = 1_000_000_007

    hash_value = 0
    for char in str:
        # ord() : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
        # (a + b) % m = ((a % m) + (b % m)) % m
        # (a * b) % m = ((a % m) * (b % m)) % m
        # (a - b) % m = ((a % m) - (b % m) + p) % m
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value

def solution(string_list, query_list):
    hash_list = [polynomial_hash(str) for str in string_list]

    result = []
    for query in query_list:
        query_hash = polynomial_hash(query)
        if (query_hash in hash_list):
          result.append(True)
        else:
          result.append(False)

    return result

print(solution(["apple", "banana", "cherry"], ["banana", "kiwi", "melon", "apple"]))
