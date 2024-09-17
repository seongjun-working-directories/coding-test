print("\n1.")
# 예외처리 1
while True:
    try:
        age = int(input("나이 입력: "))
        print("당신의 나이는", age, "세 입니다")
        break
    except ValueError:
        print("입력값을 확인해주시기 바랍니다")


print("\n2.")
# 예외처리 2
bread = 10
try:
    people = int(input("인원: "))
    print("1인당 빵의 수:", bread/people)
    print("계산이 완료되었습니다")
except ValueError:
    print("입력값을 확인해주시기 바랍니다")
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다")
finally:
    print("에러 여부와 관계없이 실행되는 문구입니다")


print("\n3.")
# 예외처리 3
bread = 10
try:
    people = int(input("인원: "))
    print("1인당 빵의 수:", bread/people)
    print("계산이 완료되었습니다")
except:
    print("에러 종류와 관계없이 에러가 있다면 출력됩니다")
