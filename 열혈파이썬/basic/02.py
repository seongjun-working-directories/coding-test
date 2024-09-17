print("\n1.")
# 리스트
various_lists = [1, 2.0, [3, 4], ["AA", "BB"]]
print(various_lists)
del various_lists


print("\n2.")
# 리스트 연산
print([1, 2, 3] + [4, 5])  # 결과: [1, 2, 3, 4, 5]
print(['A', 'B'] * 2)  # 결과: ['A', 'B', 'A', 'B']


print("\n3.")
# 리스트 인덱싱
sample_list = [1, 2, 3]
print(sample_list[0])  # 결과: 1
sample_list[0] = -1
print(sample_list[0])  # 결과: -1
del sample_list


print("\n4.")
# 리스트 슬라이싱 => [start_idx : end_idx : step]
sample_list = [1, 2, 3, 4, 5]
print(sample_list[1:3])  # 결과: [2, 3]
print(sample_list[1:4:2])  # 결과: [2, 4]
sample_list[1:3] = [0, 0, 0, 0]
print(sample_list)  # 결과: [1, 0, 0, 0, 0, 4, 5]
del sample_list


print("\n5.")
# 리스트 슬라이싱(생략)
sample_list = [1, 2, 3, 4, 5]
print(sample_list[:3])  # 결과: [1, 2, 3]
print(sample_list[2:])  # 결과: [3, 4, 5]
sample_list[:] = []
print(sample_list)  # 결과: []


print("\n6.")
# 문자열
sample_string = "ABCDEF"
print(sample_string[2:4])  # 결과: CD
for i in sample_string:
    print(i, end=' ')
print("<= 문자열도 for문으로 사용 가능")


print("\n7.")
# 문자열 길이
sample_string = "ABCDEF"
print(len(sample_string))  # 결과: 6