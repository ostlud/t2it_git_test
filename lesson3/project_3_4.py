number  = int(input())
s = 0
ans_list = []
while number:
    ans_list.append(str(number%10)+'*10^'+str(s))
    s += 1
    number //= 10
print('+'.join(ans_list[::-1]))
    
