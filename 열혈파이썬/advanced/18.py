print("\n1.")
# 클래스 변수
class Simple:
    cv = 20  # 클래스 변수 => Simple 클래스에 속하는 변수
    def __init__(self):
        self.iv = 10  # 인스턴스 변수 => 객체별로 존재하는 변수

print(Simple.cv, Simple().cv)  # 20 20


print("\n2.")
# 클래스 변수
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    def get_count(self):
        return Counter.count

s1 = Counter()
print(s1.get_count())  # 1
s2 = Counter()
print(s1.get_count(), s2.get_count())  # 2 2


print("\n3.")
# static 메서드
# static 메서드는 첫 번째 인자로 self를 전달받지 않음
class Simple:
    data = 0
    def __init__(self):
        Simple.data += 1
    
    @staticmethod  # 다음의 메서드를 static 메서드로 선언하는 데코레이터
    def get_data():
        return Simple.data

print(Simple.get_data(), Simple().get_data())  # 0 1


print("\n4.")
# class 메서드
# class 메서드는 클래스 정보가 전달되므로, 팩토리 메서드를 만드는데 매우 적합
# 사실, static 메서드와 class 메서드의 차이는 "객체를 매개변수로 자동으로 넣어준다"의 차이
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def show(self):
        print(f"{self.year}-{self.month}-{self.day}")
    @classmethod
    def next_day(cls, today):
        return cls(today.year, today.month, today.day+1)

class KDate(Date):
    def show(self):
        print(f"KR: {self.year}-{self.month}-{self.day}")

class JDate(Date):
    def show(self):
        print(f"JP: {self.year}-{self.month}-{self.day}")

kd1 = KDate(2025, 1, 2)
kd1.show()
kd2 = KDate.next_day(kd1)
kd2.show()

jd1 = KDate(2027, 2, 16)
jd1.show()
jd2 = KDate.next_day(jd1)
jd2.show()
