print("\n1.")
# True, False는 첫 글자를 대문자로, 나머지는 소문자로 작성
print(True, False)


print("\n2.")
# if~elif~else
def if_elif_else():
    num = int(input('숫자를 입력해주시기 바랍니다: '));
    if num > 0:
        print("앙의 정수")
    elif (num < 0):
        print("음의 정수")
    else:
        print("0")
if_elif_else()


print("\n3.")
# and, or, not 연산자
print(True and False)  # 결과: False
print(True or False)  # 결과: True
print(not False)  # 결과: True


print("\n4.")
# True 또는 False로 답하는 함수
test_1 = "123"
test_2 = "abc"

# isdigit()은 문자열이 숫자로만 구성되어 있는지 확인
print(test_1.isdigit())  # 결과: True
print(test_2.isdigit())  # 결과: False

# isalpha()는 문자열이 알파벳으로만 구성되어 있는지 확인
print(test_1.isalpha())  # 결과: False
print(test_2.isalpha())  # 결과: True

# startswith, endswith
test_3 = "Hello my friends!"
print(test_3.startswith("Hello"))  # 결과: True
print(test_3.endswith("!"))  # 결과: True


print("\n5.")
# in, not in
spaghetti = "spaghetti"
print("tt" in spaghetti)  # 결과: True
print("tt" not in spaghetti)  # 결과: False

test_array = [1, 2, 3]
print(3 in test_array)  # 결과: True
print(4 not in test_array)  # 결과: True


print("\n5.")
# 0은 False의 역할을 할 수 있음
if ([]):
    print("빈 배열은 False로 인식되지 않습니다")
else:
    print("빈 배열은 False로 인식됩니다")  # O
if (0):
    print("0은 False로 인식되지 않습니다")
else:
    print("0은 False로 인식됩니다")  # O


print("\n6.")
# bool 함수는 문자열이나 리스트같은 객체들이 True인지 False인지 알 수 있게 해줌
print(bool(""))  # 결과: False


print("\n7.")
# while문
count = 0
while (count < 3):
    print(count)
    count += 1

count = 0
while (count < 10):
    if (count % 2 == 1):
        count += 1
        continue;
    if (count == 8):
        break;
    print(count)
    count += 1