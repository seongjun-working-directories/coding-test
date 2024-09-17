print("\n1.")
# 튜플
tuple_1 = (1, 2, 3)
print(tuple_1, "=> Type is", type(tuple_1))

# 단, 튜플은 값을 추가하거나 수정할 수 없음
# 즉, 처음 만들어진 상태를 그대로 사용해야 함
personal_information = [("Iron Man", 2007), ("Spider Man", 2015)]
print(personal_information[0])


print("\n2.")
# 튜플 관련 함수
tuple_2 = (1, 2, 3)
print(len(tuple_2))  # 3
print(max(tuple_2))  # 3
print(min(tuple_2))  # 1

print(3 in tuple_2)  # True
print(2 not in tuple_2)  # False
print(tuple_2 + (4, 5))  # (1, 2, 3, 4, 5)
print(tuple_2 * 2)  # (1, 2, 3, 1, 2, 3)
print(tuple_2[1:3])  # (2, 3)

for i in tuple_2:
    print(i)

tuple_3 = (1, 2, 2, 3, 3, 3)
print(tuple_3.count(2))  # 2
print(tuple_3.index(2))  # 1


print("\n3.")
# 튜플, 리스트, 그리고 range
sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)
print(tuple(sample_list))  # (1, 2, 3)
print(list(sample_tuple))  # [1, 2, 3]

# tuple()에도 마찬가지로 적용할 수 있음
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']


print("\n4.")
# range 범위 거꾸로 하기
print(list(range(10, 2, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3]
print(list(range(10, 1, -2)))  # [10, 8, 6, 4, 2]


print("\n5.")
# 매개변수에 이름 지정해서 값 전달
def who_are_you(name, age):
    print("name:", name)
    print("age:", age)
who_are_you(age=15, name="Kelvin")


print("\n6.")
# 매개변수에 default 값을 둘 때, 반드시 default 값을 갖는 매개변수가 뒤에 와야 함
def test_default(d1, d2, d3="d3", d4="d4"):
    print(d1, d2, d3, d4)
test_default("d1", "d2", "d33")  # d1 d2 d33 d4


print("\n7.")
# pass (아무 일도 하지 않는 함수)
def pass_function():
    pass
pass_function()


print("\n8.")
# 파이썬은 매개변수를 위해 별도의 메모리 공간을 할당하지 않음
# 즉, 함수 내부에서 함수 밖에 선언된 매개변수 자체의 값을 변경할 수 있음을 의미
def func(s):
    s[0] = 0
    s[-1] = 0
s = [1, 2, 3]
func(s)
print(s)  # [0, 2, 0]