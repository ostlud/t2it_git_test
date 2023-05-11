my_string = input()#'Hello, Python!!'
fun1 = lambda x: x.lower()
x = ''.join(list(map(fun1, my_string)))
print(x)
fun2 = lambda x: x.upper()
x = ''.join(list(map(fun2, my_string)))
print(x)
