# Problema 1

# def suma(*args, **param_1):
#     S = 0
#     if type(param_1) == int:
#         S +=param_1
#     for i in args:
#         if type(i) == int or type(i) == float:
#             S += i
#     return S
#
# print(suma(1, 5, -3, 'abc', [12, 56, 'cad'], 3.3))
# print(suma())
# print(suma(2, 4, 'abc', param_1 = 2))




# Problema2

# def sum_all(n):
#     if type(n) == int:
#         if n == 0:
#             return 0
#
#         return n + sum_all(n - 1)
#     else:
#         print('Introdu un nr. intreg!')
#
#
# print(sum_all(5))
#
#
# def sum_even(n):
#     if type(n) == int:
#         if n == 0:
#             return 0
#         if n % 2 == 0:
#             return n + sum_even(n - 2)
#         else:
#             return sum_even(n - 1) + sum_even(n - 3)
#     else:
#         print('Introdu un nr. intreg!')
#
#
# def sum_odd(n):
#     if type(n) == int:
#         if n <= 0:
#             return 0
#         if n % 2 == 1:
#             return n + sum_odd(n - 2)
#         else:
#             return sum_odd(n - 1) + sum_odd(n - 3)
#     else:
#         print('Introdu un nr. intreg!')
#
# print(sum_even(10))
# print(sum_odd(7))




# Problema 3

# def num_is_int(n):
#     if type(n) == int:
#         return n
#     else:
#         return 0
#
# n = input('Insert number:')
# print(type(n))
# print(num_is_int(n))
