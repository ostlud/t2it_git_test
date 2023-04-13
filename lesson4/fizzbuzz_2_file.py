f = open('fizzbuzzfile.txt', 'r')
f1 = open('fizzbuzzfile_res.txt', 'w')
line=[]
for st in f:
    st =st.split()
    fizz = int(st[0])
    buzz = int(st[1])
    n = int(st[2])
    #print(fizz, buzz, n)
    for i in range(1, n + 1):
        if not i%fizz and not i%buzz:
            line.append('FB')
        elif not i%fizz:
            line.append('F')
        elif not i%buzz:
            line.append('B')
        else:
            line.append(str(i))
    f1.write(" ".join(line))
    f1.write("\n")
    
f.close() # закриття файлу
f1.close()
