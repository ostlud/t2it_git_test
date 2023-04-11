st = input().split()
fizz = int(st[0])
buzz = int(st[1])
n = int(st[2])
for i in range(1, n + 1):
    if not i%fizz and not i%buzz:
        print('FB', end=' ')
    elif not i%fizz:
        print('F', end=' ')
    elif not i%buzz:
        print('B', end=' ')
    else:
        print(i, end=' ')
        

