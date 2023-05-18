my_dict = {"Derkach Pavlo": {'Py', 'FrontEnd', 'FullStack', 'Java'},
           "Naumov Max" : { 'Py', 'FullStack'},
           "Sergeychuk Olena": {'Py', 'FrontEnd'},
           "Samoylov Stas": {'FrontEnd'}}
#fun = list(filter(lambda x: len(x[1])>1, my_dict.items()))
#print(list(map(lambda x: x[0], fun)))

#print([a for a, b in filter(lambda x: 'Py' not in x[1], my_dict.items())])
#print(list(map(lambda x: x[0], fun1)))

fun2 = ([ x  for x,y in my_dict.items() if len(y) > 1])
print(f"2 or more group - {fun2}")
fun3 = ([ x  for x,y in my_dict.items() if 'FrontEnd' not in y])
print(f"not study FrontEnd - {fun3}")
fun4 = ([ x  for x,y in my_dict.items() if {'FrontEnd', 'Java'} & y])
print(f"study Python or Java - {fun4}")

