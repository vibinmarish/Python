def split_and_join(line):

    a=line.split()
    print(a[0].capitalize())
    s="-".join(a)

    return s



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)