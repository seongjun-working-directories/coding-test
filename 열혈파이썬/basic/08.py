print("\n1.")
# 딕셔너리 <= key:value로 저장되는 데이터
sample_dictionary1 = {
    '코카콜라': (900, '탄산'),
    '바나나우유': (1200, '유제품'),
    '비타500': (700, '비타민음료')
}
print(sample_dictionary1)

sample_dictionary2 = {
    '내가 쏠게': 'It\'s on me',
    '오랜만이야': 'Long time no see'
}
print(sample_dictionary2)


print("\n2.")
dictionary_1 = {
    'Coke': 700,
    'Soda': 500,
    'Water': 400
}
dictionary_1['Water'] = 600
print(dictionary_1['Water'])  # 600

dictionary_1['Coffee'] = 1000
print(dictionary_1)  # {'Coke': 700, 'Soda': 500, 'Water': 600, 'Coffee': 1000}

del dictionary_1['Soda']
print(dictionary_1)  # {'Coke': 700, 'Water': 600, 'Coffee': 1000}

# 주의할 점
# 1) 두 "리스트"(ex> [1, 2, 3])는 값과 순서가 모두 같아야 "==" 연산자에 대해 True이지만,
#    두 "딕셔너리"(ex> {"key":"value"})는 순서와 상관없이 저장 내용이 같으면 "==" 연산자에 대해 True임
# 2) in, not in 은 딕셔너리의 "키"에 대해서 작동함
dictionary_2 = {"hi": "hello"}
print("hi" in dictionary_2)  # True
print("hello" in dictionary_2)  # False

dictionary_3 = {
    "새우깡": 700,
    "콘치즈": 900,
    "꼬깔콘": 650
}
for i in dictionary_3:
    print(i, end=" ")  # 새우깡 콘치즈 꼬깔콘
print()