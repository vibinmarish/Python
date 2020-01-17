n=5
for i in range(0,n):
    for i in range(0,n):
        print("#",end="")

    print()

for i in range(0,n):
    for i in range(0,i+1):
        print("#",end="")
    print()

for i in range(n,0,-1):
    for i in range(i,0,-1):
        print("#",end='')
    print()

