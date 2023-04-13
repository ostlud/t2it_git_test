import sys
filename = sys.argv[1]
# далі відкриваємо файл для читання (опція 'r')
f = open(filename, 'r') # в файлі тепер file descriptor
a=[]
for line in f: # для кожного рядка у файлі
   a.append(line)
a = a[::-1]
print('\n'.join(a))
f.close() # закриття файлу
