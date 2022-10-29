def is_int():

    n = input('Introdu nr: ')

    try:
        n = int(n)
    except ValueError:
        n = 0

    return n

print(is_int())