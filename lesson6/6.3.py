qqq = ',.!?-'
my = {}
with open('loremI.txt', 'r') as ff:
    txt = ff.readlines()
    for i in txt:
        my_list = list(map(lambda a: a.lower(), i.split()))
        my_list = list(map(lambda a: a[:len(a)-1] if a[len(a)-1] in qqq else a, my_list))
        for word in my_list:
            if word not in my:
                my[word] = 1
            else:
                my[word] +=1
#print(my)
                
my = dict(sorted(my.items(), key = lambda item: item[1], reverse = True))
with open('loremRes.txt', 'w') as ff:
    for i in my.items():
        ff.write(f'{i[0]}: {i[1]}\n')
