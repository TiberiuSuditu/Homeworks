def sum_all(n):

    if n == 0:
        return 0, 0, 0

    s_all, s_even, s_odd = sum_all(n - 1)

    s_all += n

    if n % 2 == 0:
        s_even += n
    else:
        s_odd += n

    return s_all, s_even, s_odd

print(sum_all(6))