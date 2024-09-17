'''
[문제 008]
소괄호는 짝을 맞춘 열린 괄호 '(' 와 ')' 로만 구성합니다.
문제에서는 열린 괄호와 갇힌 괄호가 마구 섞인 문자열을 줍니다.
이때, 소괄호가 정상적으로 열고 닫혔는지 판별하는 solution() 함수를 구현하세요.
만약 소괄호가 정상적으로 열렸다면 True, 아니라면 False를 반환합니다.

[제약조건]
- 열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄됩니다.
- 상쇄조건은 열린 괄호가 먼저 와야 하고, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 합니다.
- 더 상쇄할 괄호가 없을 때까지 상쇄를 반복합니다.

[입출력 예]
s           result
(())()      True
((())()     False
'''
def solution_me(s):
    data = []
    for i in range(len(s)):
        if s[i] == "(":
            data.append("(")
        else:
            try:
                data.pop()
            except:
                return False
    
    if (len(data) != 0):
        return False
    return True

def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    else:
        return True

print(solution("(())()"))
print(solution("((())()"))