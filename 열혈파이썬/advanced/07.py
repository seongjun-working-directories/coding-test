print("\n1.")
# func(*iterable), func(**dict)

def many_args_1(a, b, c):
    print(a, b, c)

val_1 = [1, 2, 3]
val_2 = "123"
many_args_1(*val_1)  # 1 2 3
many_args_1(*val_2)  # 1 2 3

val_3 = dict(a=1, b=2, c=3)
many_args_1(*val_3.items())  # ('a', 1) ('b', 2) ('c', 3)


print("\n2.")
# def func(*args) : 값들이 튜플로 묶여 args에 전달됨
# def func(**args) : 값들이 딕셔너리로 묶여 args에 전달됨

def func_to_tuple(*args):
    print(args)
func_to_tuple(1, 2, 3)  # (1, 2, 3)

def func_to_dict(**args):
    print(args)
func_to_dict(a=1, b=2, c=3, d=4, e=5)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


print("\n3.")
# dict & defaultdict
sample_string = 'apple'
sample_dictionary_1 = {}
sample_dictionary_2 = {}

for i in sample_string:
    if i in sample_dictionary_1:
        sample_dictionary_1[i] += 1
    else:
        sample_dictionary_1[i] = 1
print(sample_dictionary_1)  # {'a': 1, 'p': 2, 'l': 1, 'e': 1}

# setdefault 함수는 첫번째 변수에 해당하는 키가 있으면, 키 값을 반환하고
# 없다면 딕셔너리에 k:v를 저장하고 v를 반환함
for i in sample_string:
    sample_dictionary_2[i] = sample_dictionary_2.setdefault(i, 0) + 1
print(sample_dictionary_2)  # {'a': 1, 'p': 2, 'l': 1, 'e': 1}

# defaultdict 함수는 찾는 키가 없는 경우
# 인자로 미리 등록해둔 함수가 반환하는 값을 그 키로 저장
from collections import defaultdict

print(int('35'), int())  # 35 0

sample_string = 'apple'
sample_dictionary_3 = defaultdict(int)

for i in sample_string:
    sample_dictionary_3[i] += 1
print(sample_dictionary_3)  # defaultdict(<class 'int'>, {'a': 1, 'p': 2, 'l': 1, 'e': 1})

# 사용자 정의 함수를 defaultdict의 인자로 넣을 수 있음
# from collections import defaultdict

sample_dictionary_4 = defaultdict(lambda : -1)
print(sample_dictionary_4['hi'])  # -1
print(sample_dictionary_4)  # defaultdict(<function <lambda> at 0x795f936e3d90>, {'hi': -1})


print("\n3.")
# dict & OrderedDict
from collections import OrderedDict

od = OrderedDict(a=1, b=2, c=3)
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.move_to_end('b')
print(od)  # OrderedDict([('a', 1), ('c', 3), ('b', 2)])

od.move_to_end('b', last=False)  # 매개변수 last에 False를 넣으면 맨앞으로 이동
print(od)  # OrderedDict([('b', 2), ('a', 1), ('c', 3)])