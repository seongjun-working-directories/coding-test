print("\n1.")
# set : 수학의 '집합'을 표현한 자료형
A = {'a', 'b', 'c', 'd'}
B = {'a', 'c', 'e', 'f'}
print(A-B, A&B, A|B, A^B)
# {'b', 'd'} {'a', 'c'} {'e', 'f', 'd', 'a', 'b', 'c'} {'e', 'f', 'd', 'b'}

A = set(['a', 'b', 'c', 'd'])
B = set('abcd')
print(A, B)  # {'b', 'a', 'd', 'c'} {'b', 'a', 'd', 'c'}
print(A == B)  # True
print('a' in A, 'b' not in B)  # True False

# 빈 셋은 다음과 같이 생성할 수 있음
new_set = set()
new_set.add('1')
new_set.add('2')
new_set.add('3')
print(new_set)  # {'2', '3', '1'}

new_set.remove('1')  # 삭제
print(new_set)  # {'2', '3'}
new_set.discard('2')  # 삭제
print(new_set)  # {'3'}

new_set.update('6', '7', '8')  # 추가
print(new_set)  # {'7', '8', '6', '3'}
new_set |= set(['9', '10'])  # 추가
print(new_set)  # {'9', '6', '10', '8', '7', '3'}

new_set &= set('123456')  # 겹치는 것만 보관
print(new_set)  # {'3', '6'}

# set은 중복된 값들을 허용하지 않음
tmp = [1, 1, 2, 2, 3]
tmp = list(set(tmp))
print(tmp)  # [1, 2, 3]


print("\n2.")
# frozenset : set과 같은 기능을 하지만, 수정할 수 없다는 것이 차이점
A = frozenset(['a', 'b', 'c', 'd'])
B = frozenset(['a', 'c', 'e', 'f'])

print(A)  # frozenset({'d', 'c', 'b', 'a'})
print(A-B, A|B, A&B, A^B)
# frozenset({'b', 'd'}) frozenset({'d', 'c', 'a', 'e', 'f', 'b'}) frozenset({'c', 'a'}) frozenset({'d', 'e', 'f', 'b'})

for i in A-B:
    print(i, end=", ")  # d, b,
print()


print("\n3.")
# set 컴프리핸션
s1 = {x for x in range(1, 11)}
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s2 = {x**2 for x in s1 if x<5}
print(s2)  # {16, 1, 4, 9}