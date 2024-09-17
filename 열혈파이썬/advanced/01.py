print("\n1.")
# mutable(리스트, 딕셔너리) vs immutable(문자열, 튜플)
def adder(m, n):
    m += n

sample_list = [1, 2]  # mutable
adder(sample_list, [3, 4])
print(sample_list)  # [1, 2, 3, 4]
del sample_list

sample_tuple = (1, 2)  # immutable
adder(sample_tuple, (3, 4))
print(sample_tuple)  # (1, 2)
del sample_tuple


print("\n2.")
# 매개변수로 전달된 리스트가 훼손되는 문제와 해결
def min_max_problem_function(tmp):
    tmp.sort()
    print(tmp[0], tmp[-1])

sample_list = [3, 1, 4, 2]
min_max_problem_function(sample_list)
print(sample_list)  # [1, 2, 3, 4]

def min_max_solution_function(tmp):
    val = list(tmp)
    val.sort()
    print(val[0], val[-1])

sample_list = [3, 1, 4, 2]
min_max_solution_function(sample_list)
print(sample_list)  # [3, 1, 4, 2]
del sample_list


print("\n3.")
# 객체의 비교
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(list_1 is list_2)  # False <= 'is' : 참조하는 객체가 같은가
print(list_1 == list_2)  # True <= '==' : 객체에 담긴 값이 같은가

# 파이썬은 기본적으로 얕은 복사를 수행한다
list_1 = ['John', ('man', 'usa'), [175, 23]]
list_2 = list(list_1)
print(list_1 is list_2)  # False
print(list_1[0] is list_2[0])  # True
print(list_1[1] is list_2[1])  # True
print(list_1[2] is list_2[2])  # True

# 위의 예제에서 문자열과 튜플은 문제가 되지 않지만, 리스트는 문제가 될 수 있음
list_1[2][1] = 25
print(list_2)  # ['John', ('man', 'usa'), [175, 25]]

# 따라서, 깊은 복사를 위해서는 copy 모듈의 deepcopy 메서드를 사용해야 함
from copy import deepcopy
list_1 = ['John', ('man', 'usa'), [175, 23]]
list_2 = deepcopy(list_1)
list_1[2][1] = 25
print(list_2)  # ['John', ('man', 'usa'), [175, 23]]


print("\n4.")
# 리스트 컴프리핸션 예시1
r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1]
print(r2)  # [2, 4, 6, 8, 10]

# 리스트 컴프리핸션 예시2
r1 = [1, 2, 3, 4, 5]
r2 = [x+10 for x in r1]
print(r2)  # [11, 12, 13, 14, 15]

# 리스트 컴프리핸션 예시3 (조건문 추가)
r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1 if (x % 2 == 0)]
print(r2)  # [4, 8]

# 리스트 컴프리핸션 예시4 (이중 for문 추가)
r1 = ['1', '2']
r2 = ['A', 'B']
r3 = [x+y for x in r1 for y in r2]
print(r3)  # ['1A', '1B', '2A', '2B']

# 리스트 컴프리핸션 예시5(range 사용)
print([i*j for i in range(1,3) for j in range(1,5)])
# [1, 2, 3, 4, 2, 4, 6, 8]

# 리스트 컴프리핸션 예시6
print([i*j for i in range(1,3) for j in range(1,5) if ((i*j)%2 == 0)])  # [2, 4, 2, 4, 6, 8]
# 1) for i in range(1,3)과 for j in range(1,5)에 대한 n*m을 출력한 후
# 2) if 조건문에 맞는 값만 리턴함