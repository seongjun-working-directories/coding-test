print("\n1.")
# sort
sort_1 = [3, 2, 1, 4]
sort_1.sort()
print(sort_1)  # [1, 2, 3, 4]
sort_1.sort(reverse=True)
print(sort_1)  # [4, 3, 2, 1]

sort_2 = [('Yoon', 33), ('Seong', 16), ('Kim', 21)]
def age(t):
    return t[1]
sort_2.sort(key=age)
print(sort_2)  # [('Seong', 16), ('Kim', 21), ('Yoon', 33)]
sort_2.sort(key=age, reverse=True)
print(sort_2)  # [('Yoon', 33), ('Kim', 21), ('Seong', 16)]

sort_3 = [('Yoon', 33), ('Seong', 16), ('Kim', 21)]
sort_3.sort(key=lambda t : t[1], reverse=True)
print(sort_3)  # [('Yoon', 33), ('Kim', 21), ('Seong', 16)]

sort_4 = [(1, 3), (6, 7), (5, 2)]
sort_4.sort(key=lambda t : t[0]+t[1])
print(sort_4)  # [(1, 3), (5, 2), (6, 7)]


print("\n2.")
# sorted : sort()와 같지만, 원본을 수정하는 것이 아닌 사본을 반환
sorted_1 = [('Yoon', 33), ('Seong', 16), ('Kim', 21)]
copied_sorted_1 = sorted(sorted_1, key=lambda t : t[1])
print(sorted_1)  # [('Yoon', 33), ('Seong', 16), ('Kim', 21)]
print(copied_sorted_1)  # [('Seong', 16), ('Kim', 21), ('Yoon', 33)]

# sorted는 항상 결과를 리스트로 반환됨
sorted_2 = (3, 1, 2)
copied_sorted_2 = sorted(sorted_2)
print(copied_sorted_2)  # [1, 2, 3]


print("\n3.")
# 문자열을 비교할 때 사전 편찬 순서상 뒤에 위치한 단어가 더 큼
print('가' < '나')  # True
print('A' < 'B')  # True
print('A' < 'a')  # True
print('A' < '가')  # True
print('AA' < 'AAA')  # True


print("\n4.")
# enumerate
names = ['윤나은', '김현주', '장현지', '이지선', '김석경']
eo = enumerate(names)
print([i for i in eo])  # [(0, '윤나은'), (1, '김현주'), (2, '장현지'), (3, '이지선'), (4, '김석경')]

# 단, 시작 번호를 1부터 하고자 하는 경우
eo = enumerate(names, 1)
print([i for i in eo])  # [(1, '윤나은'), (2, '김현주'), (3, '장현지'), (4, '이지선'), (5, '김석경')]

# 활용 예제
example = {k:v for k, v in enumerate(sorted(names), 1)}
print(example)  # {1: '김석경', 2: '김현주', 3: '윤나은', 4: '이지선', 5: '장현지'}
