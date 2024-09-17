print("\n1.")
# 정보 은닉
class Info:
    # 변수 이름 앞에 언더바 두 개를 이어서 붙이면(__),
    # 외부에서 직접 접근이 불가능해짐
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def add_age(self, age):
        if (age < 0):
            print("양의 정수를 입력해주시기 바랍니다.")
        else:
            self.__age += age
    def __str__(self):
        return '{}: {}'.format(self.__name, self.__age)

info = Info('Holmes', 23)
# info.__age += 1  # AttributeError: 'Info' object has no attribute '__age'
print(info)  # Holmes: 23
info.add_age(1)
print(info)  # Holmes: 24

# 파이썬 프로그래머는 관례상 언더바 한 개(_)가 붙은 변수에 직접 접근하지 않는 관례가 있음
class Info:
    # 변수 이름 앞에 언더바 두 개를 이어서 붙이면(__),
    # 외부에서 직접 접근이 불가능해짐
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def add_age(self, age):
        if (age < 0):
            print("양의 정수를 입력해주시기 바랍니다.")
        else:
            self._age += age
    def __str__(self):
        return '{}: {}'.format(self._name, self._age)

info = Info('Holmes', 23)
# 실제로 접근은 가능하지만, 관례상 '_'가 앞에 붙은 변수는 접근하지 않도록 약속함
info._age += 1
print(info)  # Holmes: 24
info.add_age(1)
print(info)  # Holmes: 25


print("\n2.")
# __dict__ : 객체의 변수 정보를 담고 있는 딕셔너리
class Info:
    def __init__(self, name, age):
        self._name = name
        self._age = age

info = Info("Calvin", 23)
print(info.__dict__)  # {'_name': 'Calvin', '_age': 23}

# 즉, 객체 내 변수 값은 __dict__를 통해 관리가 됨
class Data:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return 'data: {}'.format(self.data)

d = Data(10)
print(d)  # data: 10
d.__dict__['data'] = 15
print(d)  # data: 15

class Data:
    def __init__(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

d = Data(20)
print(d.get_data())  # 20
print(d.__dict__)  # {'_Data__data':20}

d.__data = 21
print(d.get_data())  # 20
print(d.__dict__)  # {'_Data__data': 20, '__data': 21}

# 언더바 두개가 붙인 속성은 사실 감춰지는 것이 아닌 이름이 바뀌어 저장되는 것
# 이 바뀐 이름을 __dict__로 찾아 변경하면 해당 변경은 막을 수 없음
d._Data__data = 21
print(d.get_data())  # 21
print(d.__dict__)  # {'_Data__data': 21, '__data': 21}