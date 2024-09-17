print("\n1.")
# 연산자 오버로딩
class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    def __add__(self, money):
        print("__add__ 호출!")
        self.balance += money
    def __sub__(self, money):
        print("__sub__ 호출!")
        self.balance -= money
    def __call__(self):  # 계좌상황을 문자열로 변환
        print("__call__ 호출!")
        return str(self.id) + ": " + str(self.balance)

account = Account(1103122123, 100000000)
account + 10000  # __add__ 호출!
account - 5000  # __sub__ 호출!
print(account())  # __call__ 호출!
                  # 1103122123: 100005000


print("\n2.")
# 연산자 오버로딩
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    def __call__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

v1 = Vector(3, 3)
v2 = Vector(7, 7)
v3 = v1+v2

# 1번 예제와 달리, 연산자가 가지고 있는 기본 기능 및 결과를 유지(권장)
print(v1())  # Vector(3, 3)
print(v2())  # Vector(7, 7)
print(v3())  # Vector(10, 10)


print("\n3.")
# __str__
class Sample:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return 'Sample-{}'.format(self.i)

sample = Sample('A')
print(sample)  # Sample-A


print("\n4.")
# in-place 형태의 연산자 오버로딩
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):  # 새로운 객체 생성 및 반환
        return Vector(self.x+other.x, self.y+other.y)
    def __iadd__(self, other):  # 기존 객체의 값을 변경 => '+='에 대응
        self.x += other.x
        self.y += other.y
        return self  # in-place 연산자 오버로딩 시 반드시 self 변환
    def __call__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

v1 = Vector(3, 3)
v2 = Vector(7, 7)
print(v1(), id(v1))  # Vector(3, 3) 127144008907552
v1 += v2
print(v1(), id(v1))  # Vector(10, 10) 127144008907552


print("\n5.")
# 연산자 오버로딩 정리
class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
    def __iadd__(self, money):
        self.balance += money
        return self
    def __isub__(self, money):
        self.balance -= money
        return self
    def __str__(self):
        return 'id: {}, balance: {}'.format(self.id, self.balance)

account = Account('Jameson', 1000000000)
account += 130
account -= 40
print(account)  # id: Jameson, balance: 1000000090