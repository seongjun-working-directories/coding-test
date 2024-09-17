print("\n1.")
# __slots__ : 변수의 '개수'와 '이름'을 제한할 수 있음
import timeit

class Point_3D_Dict:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

start = timeit.default_timer()

p_dict = Point_3D_Dict(1, 2, 3)
for i in range(2000):
    for j in range(2000):
        p_dict.x += 1
        p_dict.y += 2
        p_dict.z += 3
print(p_dict)

stop = timeit.default_timer()
print(stop - start)  # 1.6381251049999719

class Point_3D_Slot:
    # 이 문장만 차이가 있음
    # __slots__ 사용시 객체별로 __dict__가 생기지 않음
    # 대신, 클래스당 하나의 __slots__만 생성됨
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

start = timeit.default_timer()

p_slot = Point_3D_Slot(1, 2, 3)
for i in range(2000):
    for j in range(2000):
        p_slot.x += 1
        p_slot.y += 2
        p_slot.z += 3
print(p_slot)

stop = timeit.default_timer()
print(stop - start)  # 1.4147743529999843

# 다음과 같은 연산 시 오류 발생
# p_slot.w = 1  # AttributeError


print("\n2.")
# 데코레이터
def adder_with_decorator(func):
    def inner_adder(*args):
        print(*args, sep=" + ", end=' ')
        print(f"= {func(*args)}")
    return inner_adder

@adder_with_decorator
def adder(n1, n2):
    return n1 + n2

@adder_with_decorator
def adder_three(n1, n2, n3):
    return n1 + n2 + n3

adder(3, 4)  # 3 + 4 = 7
adder_three(3, 5, 6)  # 3 + 5 + 6 = 14


print("\n2.")
# 이중 데코레이터
def decorator_1(func):
    def inner():
        print("deco1")
        func()
    return inner

def decorator_2(func):
    def inner():
        print("deco2")
        func()
    return inner

@decorator_1
@decorator_2
def simple():
    print("simple")

simple()
# deco1
# deco2
# simple