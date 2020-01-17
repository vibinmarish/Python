for i in range(6,0,-2):
    print(i,end=" ")
print()

for i in reversed(range (0,6)):
    print(i,end=" ")
print()

x=[i**2 for i in reversed(range(0,6))]
print(x)
