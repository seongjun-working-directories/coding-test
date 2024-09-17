'''
[문제 009]
10진수를 받아 2진수로 반환하는 solution() 함수를 작성하세요.

[제약조건]
- 없음

[입출력 예]
decimal     result
10          1010
27          11011
12345       11000000111001
'''
def solution_me(num):
    result = []
    while(True):
        if (num <= 1):
            result.append(1)
            break
        result.append(num%2)
        num = int(num/2)
    
    data = ""
    for i in range(len(result)):
        data += str(result.pop())
    return data

def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2
    
    binary = ""
    while stack:
        binary += stack.pop()
    return binary

print(solution(12345))
print(solution(27))