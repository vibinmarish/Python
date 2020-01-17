def swap_case(s):
    lis = []
    for i in range(len(s)):
        if s[i].isupper():
            lis.append(s[i].lower())
        else:
            lis.append(s[i].upper())
    s = ""
    s = "".join(map(str, lis))
    return s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)