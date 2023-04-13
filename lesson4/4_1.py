list_temp = [11, 25, 36, 45]
s = 0
for i in list_temp:
    s += i
print(s)

i = s = 0
while i < len(list_temp):
    s += list_temp[i]
    i += 1
print(s)
