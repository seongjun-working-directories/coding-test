# 생성자 __init__
class AgeInfo:
    def __init__(self, age):
        self.age = age
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age

kelvin = AgeInfo(15)
print(kelvin.get_age())  # 15