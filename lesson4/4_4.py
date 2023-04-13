x= int(input())
list_temp = [5, 10, 20, 50, 100, 200, 500, 1000]
list_temp = list_temp[::-1]
for i in list_temp:
    if x//i:
        print ('banknote -', i,'count - ',x//i)
    x %= i
    
