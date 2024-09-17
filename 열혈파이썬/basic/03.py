print("\n1.")
# 리스트 관련 함수 min, max
list_1 = [1, 3, 5]
print(len(list_1))  # 결과: 3
print(max(list_1))  # 결과: 5
print(min(list_1))  # 결과: 1


print("\n2.")
# 리스트 관련 함수 remove
list_2 = ['A', 'B', 'C', 'D']
list_2.remove('B')
print(list_2)  # 결과: ['A', 'C', 'D']


print("\n3.")
# 리스트 관련 함수 append, extend
list_3 = [1, 2, 3]
list_3.append([4, 5])
print(list_3)  # 결과: [1, 2, 3, [4, 5]]
list_3.extend([6, 7])
print(list_3)  # 결과: [1, 2, 3, [4, 5], 6, 7]
print("append 함수는 하나의 요소로, extend 함수는 다른 리스트 내용 전체를 각각의 요소로 맨 뒤에 추가할 때 사용")


print("\n4.")
# 리스트 관련 함수 insert, clear
list_4 = [1, 2, 4]
list_4.insert(2, 3)  # list_4[앞 인자]에 뒤 인자 값을 저장(원래 있던 요소들은 하나씩 뒤로 밀어냄)
print(list_4)  # 결과: [1, 2, 3, 4]
list_4.clear()  # list_4를 빈 배열로 만듦
print(list_4)  # 결과: []


print("\n5.")
# 리스트 관련 함수 append
list_5 = []
list_5.append(1)
list_5.append(9)
print(list_5)  # 결과: [1, 9]


print("\n6.")
# 리스트 관련 함수 pop
list_6 = [1, 2, 3]
popped_data = list_6.pop(2)  # 인자로 들어온 값의 "인덱스"에 해당하는 값을 반환 후 삭제
print(popped_data)  # 결과: 3
print(list_6)  # 결과: [1, 2]


print("\n7.")
# 리스트 관련 함수 pop
list_7 = [1, 2, 1, 2, 1]
print(list_7.count(1))  # 결과: 3
print(list_7.index(2))  # 결과: 1 <- 처음 등장하는 값 기준의 인덱스를 반환