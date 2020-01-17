if __name__ == '__main__':
    n = int(input())
    arr =[2,3,6,6,5]
  #  for a in range(0,n):
  #      arr.append(int(input()))

maxm=arr[0]
for i in range(1,n):
    if arr[i]>maxm:
        sec=maxm
        maxm=arr[i]
    elif arr[i]> sec and arr[i]!=maxm:
        sec=arr[i]
print(sec)
