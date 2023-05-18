my_dict = {"Derkach Pavlo":[7, 8, 9],
           "Naumov Max" : [10, 11, 12, 9, 10],
           "Sergeychuk Sergiy": [6, 10, 11, 2, 12]}

def sered (x):
    return sum(x)/len(x)
m_x = ['', 0]
m_n = ['', 15]
for k, v in my_dict.items():
    if sered(v)> m_x[1]:
        m_x[0], m_x[1] = k, sered(v)
    if sered(v)< m_n[1]:
        m_n[0], m_n[1] = k, sered(v)

print(m_x)
print(m_n)
