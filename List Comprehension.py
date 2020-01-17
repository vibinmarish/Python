a=[1,2]
a.append(3)
print(a)
c=[]
for i in a:
     c.append(i*2)
print(c)
d=[i*2 for i in a]
print (d)