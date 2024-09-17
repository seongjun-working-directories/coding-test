print("\n1.")
# 제너레이터
def number_generator():
    print('A', end=' ')
    yield print('1')  # 첫번째 next 호출에서 이 코드까지 실행
    print('B', end=' ')
    yield print('2')  # 두번째 next 호출에서 이 코드까지 실행
    print('C', end=' ')
    yield print('3')  # 세번째 next 호출에서 이 코드까지 실행

gen = number_generator()
print(type(gen))  # <class 'generator'>

next(gen)  # A 1
next(gen)  # B 2
next(gen)  # C 3
# next(gen)  # StopIteration Error


print("\n2.")
# 제너레이터는 반환할 값들을 미리 만들어서 저장하지 않음
from sys import getsizeof

# 제너레이터 사용하지 않은 경우
def pow_not_generator(list_param):
    tmp = []
    for i in list_param:
        tmp.append(i**2)
    return tmp
result_not_generator = pow_not_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in result_not_generator:
    print(i, end=' ')
print()
print(getsizeof(result_not_generator))  # 184

# 제너레이터 사용한 경우
def pow_generator(list_param):
    for i in list_param:
        yield i ** 2
result_generator = pow_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in result_generator:
    print(i, end=' ')
print()
print(getsizeof(result_generator))  # 104


print("\n3.")
# yield from
# 1
def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    for i in ns:
        yield i
g = get_nums()
print(next(g))  # 0
print(next(g))  # 1

# 2
def get_nums_with_yield_from():
    ns = [0, 1, 0, 1, 0, 1]
    yield from ns
g = get_nums_with_yield_from()
print(next(g))  # 0
print(next(g))  # 1


print("\n4.")
# 제너레이터 표현식
def show_doubled_data(s):
    for i in s:
        print(i, end=' ')
    print()
g_list = [2*i for i in range(1, 10)]
show_doubled_data(g_list)

# 제너레이터 표현식은 [...]에서 (...)로 바뀔뿐
# 그 안을 채우는 방법은 리스트 컴프리핸션과 동일
g_generator = (2*i for i in range(1, 10))
show_doubled_data(g_generator)