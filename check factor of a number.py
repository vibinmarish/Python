g = []
for i in range(0, 3):
    a = int(input('Enter elements'))
    g.append(a)
n = int(input("Enter a number"))
for i in range(len(g)):
    if g[i] % n == 0:
        print(g[i])
