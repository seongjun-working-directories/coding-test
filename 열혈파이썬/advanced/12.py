print("\n1.")
# 부모 클래스가 갖는 모든 메서드는 자식 클래스에도 포함됨
# 자식 클래스는 별도의 메서드를 가질 수 있음
class Super:
    def run(self):
        print("RUN")

class Sub(Super):
    def jump(self):
        print("JUMP")

def main():
    sub = Sub()
    sub.run()  # RUN
    sub.jump()  # JUMP

main()


print("\n2.")
# 두 클래스를 동시에 상속 가능
# 단, 단일 상속 권장
class One:
    def one(self):
        print("one")

class Two:
    def two(self):
        print("two")

class Three(One, Two):
    def three(self):
        print("three")

three = Three()
three.one()  # one
three.two()  # two
three.three()  # three


print("\n3.")
# 메서드 오버라이딩
class Top:
    def top(self):
        print('from top')
    
class Bottom(Top):
    def top(self):
        print('from bottom')
    def make_top(self):
        super().top()

def main():
    s = Bottom()
    s.top()  # from bottom
    s.make_top()  # from top

main()


print("\n4.")
# __init__ 메서드의 오버라이딩
class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fuel(self, f):
        self.fuel += f
    def show_info(self):
        print(f"id: {self.id}")
        print(f"fuel: {self.fuel}")

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    def add_cargo(self, c):
        self.cargo += c
    def show_info(self):
        super().show_info()
        print(f"cargo: {self.cargo}")

def main():
    c = Truck("01-1u8901", 100, 0)
    c.add_fuel(200)
    c.drive()
    c.drive()
    c.add_cargo(10)
    c.show_info()

main()
# id: 01-1u8901
# fuel: 280
# cargo: 10
