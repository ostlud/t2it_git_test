def my_zip (*x):
    y = min(list(map(len, x )))
    yy = list([] for i in range(y))
    for i in x:
        for ii,jj in enumerate(i[:y]):
            yy[ii].append(jj)
    return tuple(map(tuple, yy))
    

print(my_zip([1,2,3,4], [5,6,7,8],[0,0 ,0]))
