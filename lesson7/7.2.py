fun = lambda x: x**2

def isprime (x):
    if x in {1, 2, 3, 5, 7}:
        return True
    else:
        for i in range(2,round(x**0.5) + 1):
            if not x%i:
                return False
        return True


my_list = list(filter(isprime, range(1, 51)))
my_list = list(map(fun, my_list))
print(my_list)
