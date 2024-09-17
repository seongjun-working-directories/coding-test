print("\n1.")
# format
fs_1 = '{0}...{1}...{2}'
ms_1 = fs_1.format("1", "2", "3")
print(ms_1)  # 1...2...3

ms_2 = 'Hello~ {0}!'.format("Kevin")
print(ms_2)  # Hello~ Kevin!

ms_3 = '{2} {0} {1}'.format("ㄱ", "ㄴ", "ㄷ")
print(ms_3)  # ㄷ ㄱ ㄴ

ms_4 = '{} {} {}'.format("1", "2", "3")
print(ms_4)  # 1 2 3

fs_5 = ['Robot', 123, 'Box']
ms_5 = '{0}...{1}...{2}'.format(*fs_5)
print(ms_5)  # Robot...123...Box


print("\n2.")
# 가장 손쉬운 문자열 결합 => f-string
number_1 = 1
number_2 = 2
print(f"{number_1}+{number_2}={number_1+number_2}")  # 1+2=3
