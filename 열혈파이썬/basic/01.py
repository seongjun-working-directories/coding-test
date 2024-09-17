print("\n1.")
# 파이썬의 특징적인 대입 방법
x, y = "Apple", "Banana"
x, y = y, x
print(x, y)  # 결과: Banana Apple


# 변수 개체를 삭제하는 방법
del x
del y
# print(x, y)  # NameError: name 'x' is not defined


print("\n2.")
# 파라미터 없는 함수
def start_python_with_snake_case():
    print(
        "파이썬의 네이밍 컨벤션은",
        "자바와 달리 각 단어를 밑줄(_)로 구분하여 표기하는 스네이크 케이스를 따른다."
    )
start_python_with_snake_case()


print("\n3.")
# 파라미터 있는 함수
def adder(number1, number2):
    return number1 + number2
print(adder(50, 50))  # 결과: 100


print("\n4.")
# 사용자에게 값을 입력받는 방법
for i in range(10):
    info = "반복문을 10회 이내에 종료하려면 'q' 버튼을 누르세요(" + str(i+1) + "/10): "
    q_button_to_quit = input(info)
    if (q_button_to_quit == 'q'):
        break


print("\n5.")
# input 함수는 입력된 내용을 하나의 문자열로 묶어서 반환
# eval 함수는 문자열 형식을 입력받아 동적으로 계산하여 출력해주는 함수
radius = eval(input("radius: "))
area = (radius ** 2) * 3.14
print(area)


print("\n6.")
# eval 함수는 전달된 문자열의 내용을 평가 및 해석하기 때문에 보안에 취약할 수 있음
def written_by_user():
    return 'It can be hacked!'
info = "'written_by_user()' 를 입력하면 프로그램에 정의된 written_by_user 함수가 실행됨: "
result = eval(input(info))
print(result)


print("\n7.")
# 배열을 사용한 for ~ in ... 반복문
for i in [0, 1, 2]:
    print(i, end='-')
print(" <= 배열을 사용한 반복문")


print("\n8.")
# for ~ in ... + range(start, end, step)
for i in range(1, 3):
    print(i)  # 1과 2가 출력됨
for i in range(3):
    print(i)  # 0, 1, 2가 출력됨


print("\n9.")
# int / float
print(type(3), type(3.0))  # 결과: <class 'int'> <class 'float'>
num = 10
float_num = float(num)
print(float_num)  # 결과: 10.0
integer_num = int(float_num)
print(integer_num)  # 결과: 10


print("\n10.")
# 파이썬에서도 복합 대입 연산자를 사용 가능
val1 = 1
val2 = 2
val1 += val2
print(val1)  # 결과: 3