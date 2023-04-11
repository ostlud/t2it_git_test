number  = int(input())
for i in range (1, number//2 + 1):
    if not number%i:
        print (i, end = ' ')
print(number)
    
