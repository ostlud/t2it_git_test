number  = int(input())
react = 'No'
if number%2:
    if not number%3 and not number%5:
        if number%10:
            react = 'YES'
print(react)
