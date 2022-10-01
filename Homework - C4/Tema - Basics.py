# Problema 1

# def suma(*args, **kwargs):  # kwargs este Optional Variable-Length Arguments
#                             # kwargs este de tip dict
#     s = 0
#     for i in args:
#         if type(i) == int or type(i) == float:   # if type(i) in [int, float]
#             s += i
#     return s
# 
# 
# print(suma(1, 5, -3, 'abc', [12, 56, 'cad']))
# print(suma())
# print(suma(2, 4, 'abc', param_1=2))





# Problema2

# VARIANTA 1

# def sum_all(n):
#     if isinstance(n, int):
#         if n == 0:
#             return 0
#         else:
#             return n + sum_all(n - 1)
#     else:
#         return None

# n = int(input('Numar -> '))
#
# print('Suma numerelor intregi 0 -> n:', sum_all(n))
#
# s_impare = 0
# s_pare = 0
#
# if n % 2 == 0:
#     for i in range(0, n + 1):
#         s_impare += (i // 2)
#     s_pare = sum_all(n) - s_impare
# else:
#     for i in range(0, n + 1):
#         s_pare += (i // 2)
#     s_impare = sum_all(n) - s_pare
#
# print('Suma numerelor pare este:', s_pare)
# print('Suma numerelor impare este:', s_impare)

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




# VARIANTA 2

# def f2(n):
#     if n == 0:
#         return 0, 0, 0  # total, even, odd
#
#     total, even, odd = f2(n-1)
#     total += n
#
#     if n % 2 == 0:
#         even += n
#     else:
#         odd += n
#
#     return total, even, odd
#
#
# n_total, n_even, n_odd = f2(5)
# print('total = ', n_total)
# print('even = ', n_even)
# print('odd = ', n_odd)





# VARIANTA 1

# def num_is_int(n):
#     if n.isnumeric():
#         return n
#     else:
#         return 0
#
# n = input('Nr: ')
#
# print(num_is_int(n))


# VARIANTA 2

# def f3():
#     x = input()
#
#     try:
#         x = int(x)
#     except ValueError:
#         x = 0
#
#     return x
#
#
# print(f3())



