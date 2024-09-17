print("\n1.")
# Iterable 객체와 Iterator 객체
sample_list = [1, 2, 3, 4]
sample_iterator = iter(sample_list)  # 튜플과 문자열에도 iter()를 사용할 수 있음
print(next(sample_iterator))  # 1
print(next(sample_iterator))  # 2
sample_list.pop(2)  # sample_iterator는 sample_list를 참조하므로, sample_list 값이 바뀌면 sample_iterator의 순서도 바뀜
print(next(sample_iterator))  # 4
# print(next(sample_iterator))  # StopIteration Error

# dir(): 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열
print(dir([1, 2]))
# [
#     '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
#     '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#     '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
#     '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#     '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
#     '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
#     'remove', 'reverse', 'sort'
# ]

# hasattr(): object에 attribute_name이 있는지 확인
print(hasattr("hi", "__iter__"))  # True

# iterable 객체와 iterator 객체 모두 for 루프의 반복 대상이 될 수 있음
sample_iterator2 = iter([1, 2])
for i in sample_iterator2:
    print(i)


print("\n2.")
# 함수는 함수를 반환할 수 있음
def outer(n):
    def inner(x):
        return x ** n
    return inner

f2 = outer(2)  # 제곱을 반환하는 함수
f3 = outer(3)  # 세제곱을 반환하는 함수
print(f2(2))  # 4
print(f3(2))  # 8


print("\n3.")
# 람다
printer = lambda string_1 : print(string_1)
printer("Hello")

adder = lambda number_1, number_2 : number_1 + number_2
printer(adder(1, 2))

hello = lambda : print("Hello")
hello()