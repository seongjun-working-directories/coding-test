print("\n1.")
# 문자열 함수 count, lower, upper
string_1 = "AbAbAb"
print(string_1.count("Ab"))  # 결과: 3
print(string_1.lower())  # 결과: ababab
print(string_1.upper())  # 결과: ABABAB


print("\n2.")
# 문자열 함수 strip, rstrip, lstrip (공백 제거)
string_2 = " . "
print(string_2.strip())  # 결과: "."
print(string_2.rstrip())  # 결과: " ."
print(string_2.lstrip())  # 결과: ". "


print("\n3.")
# 문자열 함수 replace
string_3 = "Hi! Hello~~"
print(string_3.replace("H", "h"))  # 결과: hi! hello~~
print(string_3.replace("H", "h", 1))  # 결과: hi! Hello~~


print("\n4.")
# 문자열 함수 split
string_4 = "This_is_python"
print(string_4.split("_"))  # 결과: ['This', 'is', 'python']


print("\n5.")
# 문자열 함수 find, rfind
string_5 = "An Apple Is An Apple."
print(string_5.find("Apple"))  # 결과: 3 <= 인자로 주어진 값이 문자열에 있으면 그 위치의 인덱스 값을 반환, 없으면 -1 반환
print(string_5.rfind("Apple"))  # 결과: 15 <= rfind는 find와 같은 기능이지만, 뒤에서부터 찾는다는 차이점이 있음


print("\n6.")
# 이스케이프 문자 => \n, \t, \', \", \\
print("\n \t \' \" \\")


print("\n6.")
# 파이썬의 다양한 삭제 방법
sample_list = [1, 2, 3]
sample_list.clear()
print(sample_list)  # 결과: []

sample_list = [1, 2, 3]
sample_list[:] = []
print(sample_list)  # 결과: []

sample_list = [1, 2, 3]
sample_list[2:] = []
print(sample_list)  # 결과: [1, 2]

sample_list = [1, 2, 3]
del sample_list[2:]
print(sample_list)  # 결과: [1, 2]

sample_list = [1, 2, 3]
del sample_list[:]
print(sample_list)  # 결과: []

sample_list = [1, 2, 3]
del sample_list
# print(sample_list)  # NameError: name 'sample_list' is not defined