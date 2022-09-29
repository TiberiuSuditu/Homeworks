# Problema 1

# def suma(*args, **param_1):  # param_1 este Optional Variable-Length Arguments
#                              # param_1 este de tip dict
#     S = 0
#     for i in args:
#         if (type(i) == int or type(i) == float):
#             S += i
#     return S

# print(suma(1, 5, -3, 'abc', [12, 56, 'cad']))
# print(suma())
# print(suma(2, 4, 'abc', param_1 = 2))




# Problema2

# def sum_all(n):
#     if type(n) == int:
#         if n == 0:
#             return 0
#         else:
#             return n + sum_all(n - 1)

# n = int(input('Numar -> '))

# print('Suma numerelor intregi 0 -> n:', sum_all(n))

# S_impare = 0
# S_pare = 0

# if n % 2 == 0:
#     for i in range (0, n + 1):
#         S_impare += (i // 2)
#     S_pare = sum_all(n) - S_impare
# else:
#     for i in range (0, n + 1):
#         S_pare += (i // 2)
#     S_impare = sum_all(n) - S_pare

# print('Suma numerelor pare este:', S_pare)
# print('Suma numerelor impare este:', S_impare)

# CUM AM GANDIT-O?
# 21 // 2 = 10
# 1 + 3 + 5 = 9 ( pare = impare || toate nr. // 2 -> insumate )
# 2 + 4 + 6 = 12
# S_pare = sum_all(n) - S_impare

# 28 / 2 = 14 ( 14 )
# 1 + 3 + 5 + 7 = 16
# 2 + 4 + 6 = 12 ( pare < impare || toate nr. // 2 -> insumate )
# S_impare = sum_all(n) - S_pare

# 36 / 2 = 18 ( 18 )
# 1 + 3 + 5 + 7 = 16 ( pare = impare || toate nr. // 2 -> insumate )
# 2 + 4 + 6 + 8 = 20
# S_pare = sum_all(n) - S_impare





# Problema 3

# def num_is_int(n):
#     if n.isnumeric():
#         return n
#     else:
#         return 0

# n = input('Nr: ')

# print(num_is_int(n))



