# # functions.py 전체 import
# import functions  # functions.py가 아닌 functions로 작성함에 유의

# radius = float(input("반지름: "))
# print("넓이:", functions.ar_circle(radius))
# print("지름:", functions.ci_circle(radius))


# # functions.py에서 필요한 함수만 import
# from functions import ar_circle
# from functions import ci_circle

# radius = float(input("반지름: "))
# print("넓이:", ar_circle(radius))
# print("지름:", ci_circle(radius))

# ======================================================================

# # as로 모듈 이름 줄이기 1
# import functions as fns

# radius = float(input("반지름: "))
# print("넓이:", fns.ar_circle(radius))
# print("지름:", fns.ci_circle(radius))


# as로 모듈 이름 줄이기 2
from functions import ar_circle as ac
from functions import ci_circle as cc

radius = float(input("반지름: "))
print("넓이:", ac(radius))
print("지름:", cc(radius))