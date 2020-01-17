def solve(s):
    a = s.split("",2)
    print(a)
    z=[]
    for i in a :
        z.append(i.capitalize())
    return " ".join(z)


if __name__ == '__main__':
    s = "vibinmarish"
    print(solve(s))
