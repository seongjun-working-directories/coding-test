print("\n1.")
# map() 함수는 여러 데이터를 받아 각 요소에 함수를 적용한 결과를 반환
# map() 함수는 iterator 형태로 객체를 반환
# map(function, iterable)
pow_function = lambda n : n**2
input_list = [1, 2, 3]
output_list = list(map(pow_function, input_list))
print(output_list)  # [1, 4, 9]
del input_list, output_list

# map() 함수는 가장 짧은 길이를 가진 iterable 객체의 길이만큼 function 함수를 반복적으로 적용
sum_function = lambda n1, n2 : n1+n2
input_list1 = [1, 2, 3]
input_list2 = [1, 2]
output_list = tuple(map(sum_function, input_list1, input_list2))
print(output_list)  # (2, 4)
del input_list1, input_list2, output_list

reverse_function = lambda s : s[::-1]
input_list = ["this", "is", "python"]
output_list = list(map(reverse_function, input_list))
print(output_list)  # ['siht', 'si', 'nohtyp']


print("\n2.")
# filter()는 여러 개의 데이터로 부터 일부의 데이터만 추려낼 때 사용
# filter() 함수는 iterator 형태로 객체를 반환
# filter(조건 함수, 순회 가능한 데이터)
odd_checker = lambda n : n%2
input_list = [1, 2, 3, 4, 5]
output_list = list(filter(odd_checker, input_list))
print(output_list)  # [1, 3, 5]