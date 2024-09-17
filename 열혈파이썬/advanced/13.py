print("\n1.")
# isinstance 함수
class Empty:
    pass  # 빈 클래스 정의

empty = Empty()
print(isinstance(empty, Empty))  # True

print(isinstance([1, 2], list))  # True

# isinstance(o, c)에서 객체 o가 c를 상속하는 경우 결과는 True
class Fruit:
    pass
class Apple(Fruit):
    pass
class TheApple(Apple):
    pass

f = Fruit()
a = Apple()
t = TheApple()
print(isinstance(t, Fruit))  # True


print("\n2.")
# 파이썬의 모든 클래스는 object 클래스를 상속
class Simple:
    pass
print(isinstance(Simple(), object))  # True
print(isinstance([1, 2], object))  # True

# issubclass 함수
class A:
    pass
class AZ(A):
    pass
print(issubclass(AZ, A))  # True


print("\n3.")
# 스페셜 메서드
t = (1, 2, 3)
print(len(t), t.__len__())  # 3 3

itr = iter(t)  # t.__iter__()
for i in itr:
    print(i, end=' ')  # 1 2 3
print()


print("\n4.")
# 클래스에 스페셜 메서드 정의
class Car:
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return 'Vehicle Number: ' + self.id

c = Car("01-1u12314")
print(len(c))  # 10
print(str(c))  # Vehicle Number: 01-1u12314


print("\n5.")
# iterator 객체 생성
class Coll:
    def __init__(self, d):
        self.ds = d
        self.cc = 0
    def __next__(self):
        if (len(self.ds) <= self.cc):
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc-1]

coll = Coll([1, 2, 3])
while True:
    try:
        i = next(coll)
        print(i, end=' ')  # 1 2 3
    except StopIteration:
        break


print("\n6.")
# iterator 인 동시에 iterable 객체 생성
# iterable 객체를 인자로 전달하면서 iter 함수를 호출하면 iterator 객체가 됨
class Coll2:
    def __init__(self, d):
        self.ds = d
    def __next__(self):
        if (len(self.ds) <= self.cc):
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc-1]
    def __iter__(self):  # 해당 메서드를 정의하여 iterable 객체 생성
        self.cc = 0  # next 호출 횟수 초기화
        print("__iter__ 호출!")
        return self  # 이 객체를 그대로 반환

coll2 = Coll2([1, 2, 3])
for i in coll2:
    print(i, end=' ')  # __iter__ 호출!
print()                # 1 2 3
for i in coll2:
    print(i, end=' ')  # __iter__ 호출!
print()                # 1 2 3
# for 문에 coll2 가 사용될 때마다 __iter__ 함수가 호출되는 것을 확인 가능