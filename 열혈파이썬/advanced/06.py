print("\n1.")
# 딕셔너리 생성 방법
dict_1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict_2 = dict([('a', 1), ('b', 2), ('c', 3)])

dict_3 = dict(a=1, b=2, c=3)

dict_4 = dict(
    zip(['a', 'b', 'c'], [1, 2, 3])
)

print(dict_1 == dict_2 == dict_3 == dict_4)  # True


print("\n2.")
# zip 함수
z1 = zip(['a', 'b', 'c'], [1, 2, 3])
for i in z1:
    print(i, end=' ')  # ('a', 1) ('b', 2) ('c', 3)
print()

z2 = zip('abc', [1, 2, 3])
for i in z2:
    print(i, end=' ')  # ('a', 1) ('b', 2) ('c', 3)
print()

# zip 함수는 dictionary 뿐만 아니라 tuple, list를 만들 수 있음
print(
    list(zip(['a', 'b', 'c'], [1, 2, 3]))  # [('a', 1), ('b', 2), ('c', 3)]
)
print(
    tuple(zip(['a', 'b', 'c'], [1, 2, 3]))  # (('a', 1), ('b', 2), ('c', 3))
)

print(
    list(zip(
        'abc',
        (1, 2, 3),
        ['가', '나', '다']
    ))  # [('a', 1, '가'), ('b', 2, '나'), ('c', 3, '다')]
)


print("\n3.")
# 딕셔너리 루핑
d1 = dict(a=1, b=2, c=3)
for k in d1:
    print(k, d1[k], end=", ")  # a 1, b 2, c 3,
print()

# dict.keys(), dict.values(), dict.items()
print(d1.keys())  # dict_keys(['a', 'b', 'c'])
print(d1.values())  # dict_values([1, 2, 3])
print(d1.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

for key, value in d1.items():
    print(key, value, end=', ')  # a 1, b 2, c 3,
print()

for kv in d1.items():
    print(kv, end=", ")  # ('a', 1), ('b', 2), ('c', 3),
print()


print("\n4.")
# 딕셔너리 컴프리핸션
sample_list = [1, 2, 3, 4, 5]
dc1 = [x*2 for x in sample_list]
print(dc1)  # [2, 4, 6, 8, 10]

sample_dictionary = dict(a=1, b=2, c=3)
dc2 = {k+"a": v*2 for k, v in sample_dictionary.items()}
print(dc2)  # {'aa': 2, 'ba': 4, 'ca': 6}

sample_dictionary['d'] = 4
sample_dictionary['e'] = 5
print(sample_dictionary)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dc3 = {k+"a": v*3 for k, v in sample_dictionary.items() if v%2}
print(dc3)  # {'aa': 3, 'ca': 9, 'ea': 15}

ks = list('abcde')
print(ks)  # ['a', 'b', 'c', 'd', 'e']
vs = list(range(1, 5))
print(vs)  # [1, 2, 3, 4]

d = {k:v for k, v in zip(ks, vs)}
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d = {k:v for k, v in zip(ks, vs) if v%2}
print(d)  # {'a': 1, 'c': 3}
