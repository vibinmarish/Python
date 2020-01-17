a='Vibin'
b=[a[i:j] for i in range(len(a)) for j in range(i+1,len(a)+i)]
print(b)