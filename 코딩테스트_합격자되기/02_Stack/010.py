'''
[문제 010] - https://programmers.co.kr/learn/courses/30/lessons/76502
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
(), [], {} 는 모두 올바른 괄호 문자열입니다.

만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다.
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.

대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

[제약조건]
- s의 길이는 1 이상 1000 이하 입니다.

[입출력 예]
s           result
"[](){}"    3
"}]()[{"    2
"[)(]"      0
"}}}"       0
'''
def solution_me(s):
    count = 0

    # s를 하나씩 뒤로 밀며, 조건을 만족하는지 확인
    for i in range(len(s)):
        stack = []
        tmp = s[i:] + s[:i]

        # tmp에 대해 스택을 적용
        try:
            for char in tmp:
                if (char == "(") or (char == "{") or (char == "["):
                    stack.append(char)
                else:
                    matcher = stack.pop()
                    if matcher == "(":
                        if not (char == ")"):
                            raise Exception("MISMATCH")
                    if matcher == "{":
                        if not (char == "}"):
                            raise Exception("MISMATCH")
                    if matcher == "[":
                        if not (char == "]"):
                            raise Exception("MISMATCH")
        except:
            continue

        if len(stack) == 0:
            count += 1
    
    return count

def solution(s):
    answer = 0

    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i + j) % n]  # 인덱스를 활용해 문자열 밀기를 구현
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    break
            
                # 닫힌 괄호가 스택의 top과 짝이 맞는지 비교
                if c ==")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        else:   # for 문이 break 에 의해 끝나지 않고 끝까지 수행된 경우
            if not stack:
                answer += 1

    return answer

print(solution("}]()[{"))
print(solution("[)(]"))