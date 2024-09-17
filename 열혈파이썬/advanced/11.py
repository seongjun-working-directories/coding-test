print("\n1.")
# 클래스와 객체
class Simple:
    def __init__(self):
        self.i = 0
    def set_i(self, i):
        self.i = i
    def get_i(self):
        return self.i

# 파이썬이 객체에 필요한 변수를 알아서 생성하는 시점은
# "객체 내에서 해당 변수를 대상으로 대입 연산을 처음 진행하는 순간"
simple_instance = Simple()
print(simple_instance.get_i())  # 0
simple_instance.set_i(200)
print(simple_instance.get_i())  # 200

# 파이썬은 객체에 변수와 메서드를 언제든 추가 및 삭제할 수 있음
simple_instance.x = 100
print(simple_instance.x)  # 100
simple_instance.sayHello = lambda : print("Hello~")
simple_instance.sayHello()  # Hello~

del simple_instance.x
del simple_instance.sayHello
# simple_instance.sayHello()  # AttributeError

# 파이썬은 인스턴스가 아닌 클래스에 객체를 추가할 수 있으며,
# 인스턴스에서 값을 찾지 못하면 클래스에 해당 속성의 값을 찾음
Simple.num = 1
s1 = Simple()
s1.set_i(100)
s2 = Simple()
s2.set_i(200)
print(s1.num, s1.i)  # 1 100
print(s2.num, s2.i)  # 1 200