print("\n1.")
# property
class Natural:
    def __init__(self, num):
        self.set_n(num)
    def set_n(self, num):
        if (num < 1):
            self.__n = 1
        else:
            self.__n = num
    def get_n(self):
        return self.__n
    
    # 속성 n을 참조하는 경우, get_n을 호출해서 반환
    # 속성 n을 저장하는 경우, set_n을 호출해서 반환
    n = property(get_n, set_n)

n1 = Natural(1)
n2 = Natural(2)
n3 = Natural(3)
n1.n = n2.n + n3.n
print(n1.n)  # 5

# 또는 다음과 같이 setter와 getter를 각각 지정할 수도 있음
class Natural:
    def __init__(self, num):
        self.set_n(num)
    n = property()  # 우선 프로퍼티 객체를 생성

    def set_n(self, num):
        if(num < 1):
            self.__n = 1
        else:
            self.__n = num
    n = n.setter(set_n)  # 프로퍼티 객체의 setter를 set_n()으로 지정

    def get_n(self):
        return self.__n
    n = n.getter(get_n)  # 프로퍼티 객체의 getter를 get_n()으로 지정

n1 = Natural(1)
n2 = Natural(2)
n3 = Natural(3)
n1.n = n2.n + n3.n
print(n1.n)  # 5


print("\n2.")
# 데코레이터 기반의 프로퍼티 지정
class Natural:
    def __init__(self, num):
        self.__n = num
    
    @property  # 이어서 등장하는 메서드 n을 getter로 지정하며 property 객체 생성
    def n(self):
        return self.__n
    
    @n.setter  # 이어서 등장하는 메서드를 n에 저장된 property 객체의 setter로 등록
    def n(self, num):
        if (num < 1):
            self.__n = 1
        else:
            self.__n = num

n1 = Natural(1)
n2 = Natural(2)
n3 = Natural(3)
n1.n = n2.n + n3.n
print(n1.n)  # 5


print("\n3.")
# 클로저
def maker(m):
    def inner(n):
        return m * n
    return inner

f1 = maker(2)
f2 = maker(3)
print(f1(6), f2(6))  # 12 18

# m 변수를 파이썬은 inner 함수 안에 숨겨놓고 있음
print(f1.__closure__[0].cell_contents)  # 2