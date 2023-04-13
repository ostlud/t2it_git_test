x= int(input())
list_temp = [5, 10, 20, 50, 100, 200, 500, 1000]

for id, el in enumerate(list_temp):
    for i in range(10):
        k = 10-i
        if x-k*el>=0:
            if not (x-k*el)%list_temp[id+1]:
                x = x-k*el
                print('banknote -',el,'count -',k)
                break

