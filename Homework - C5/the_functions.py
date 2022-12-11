def my_program(nr):
    try:
        nr = int(nr)
        return nr
    except ValueError:
        print("Please insert an integer value!")
        return nr

def my_palindrome(nr):
    nr = str(nr)
    if str(nr) == str(nr[::-1]):
        return "is_palindrome", True
    else:
        return "is_not_palindrome", False

def my_prime(nr):
    verify = True
    nr = int(nr)
    if nr > 1:
        for i in range(2, nr):
            if (nr % i) == 0:
                verify = False
                break
    if verify == False:
        return "is_not_prime ", verify
    else:
        return "is_prime ", verify

def my_divisors(nr):
    nr = int(nr)
    my_list = []
    for i in range(1, nr + 1):
        if nr % i == 0:
            my_list.append(i)
    print("array of divisors: -> ", my_list[:len(my_list):])
    return {"max_div: ", my_list[-2]}

def my_digits(nr):
    count = 0
    nr = int(nr)
    while nr != 0:
        nr //= 10
        count += 1
    return {"digits", count}

