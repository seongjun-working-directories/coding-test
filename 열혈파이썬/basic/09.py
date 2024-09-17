print("\n1.")
# 전역변수와 지역변수
count_1 = 100  # 전역변수
def function_1():
    count_1 = 0  # 지역변수로 새로 생성된 count_1이라고 인지하기 때문에
    print(count_1)
function_1()
print(count_1)  # 100 <= 전역변수 count_1은 아무런 영향도 받지 않음

# global 변수를 사용해서 함수 내부에서 전역변수에 접근
count_2 = 100
def function_2():
    global count_2
    count_2 = 0
    print(count_2)
function_2()
print(count_2)  # 0


print("\n2.")
# 클래스와 객체
class AgeInfo:
# python이 AgeInfo에 age가 필요함을 알고 인스턴스 변수로 넣음
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age
    # self에는 파이썬이 알아서 값을 전달하므로, 두 번째 이후의 매개변수에만 값을 전달하면 됨
    def set_age(self, age):
        self.age = age

kelvin = AgeInfo()
kelvin.age = 15
kelvin.set_age(16)
kelvin.up_age()  # kelvin 변수가 self 파라미터에 들어가는 것
print(kelvin.get_age())  # 17