print("\n1.")
# 튜플 언패킹1
list_one_two = [1, 2]
one, two = list_one_two
print(one, two)  # 1 2

tuple_a_b = ('a', 'b')
a, b = tuple_a_b
print(a, b)  # a b

numbers = (1, 2, 3, 4, 5)
n1, n2, *others1 = numbers
print(n1, n2)  # 1 2
print(others1)  # [3, 4, 5]
del n1, n2, others1

n1, *others2, n2 = numbers
print(n1, n2)  # 1 5
print(others2)  # [2, 3, 4]
del n1, n2, others2

*others3, n1, n2 = numbers
print(n1, n2)  # 4 5
print(others3)  # [1, 2, 3]


print("\n2.")
# 튜플 언패킹2
def get_dummy_tuple():
    return 1, 2, 3, 4 ,5  # 튜플은 소괄호 생략 가능
n, *numbers = get_dummy_tuple()
print(n)  # 1
print(numbers)  # [2, 3, 4, 5]

def show_numbers(n1, n2, *other_numbers):
    print(n1, n2)  # 1 2
    print(other_numbers)  # (3, 4, 5)
    # 세번째 이후 값들은 '튜플'로 묶여 other_numbers에 전달됨
show_numbers(1, 2, 3, 4, 5)

print("*는 나머지 값들을 튜플로 묶어서 이 변수에 저장하겠다는 것을 의미")


print("\n3.")
# 튜플 언패킹3
def show_man(name, age, height):
    print(name, age, height)
p = ('Yoon', 22, 171)
show_man(*p)  # 'Yoon' 22 171

p = ['Park', 21, 177]
show_man(*p)  # 'Park' 21 177


print("\n4.")
# 튜플 언패킹4
t = (1, 2, (3, 4))
a, b, (c, d) = t  # 튜플 안의 값의 구조와 동일한 형태로 변수를 선언
print(a, b, c, d)  # 1 2 3 4

ps = [('A', 1), ('B', 2)]
for alphabet, number in ps:
    print(alphabet, number)


print("\n5.")
# 네임드 튜플
from collections import namedtuple
Triangle = namedtuple('Triangle', ['bottom', 'height'])
t = Triangle(5, 7)
print(t[0], t[1])  # 5 7
print(t.bottom, t.height)  # 5 7

a, b = t
print(a, b)  # 5 7