def my_function(*args, **kwargs):
    s = 0
    for element in args:  # args e tuplu -> avem nevoie sa-l parcurgem element cu element
        if type(element) in [int, float]:
            s = s + element
    return s

print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))