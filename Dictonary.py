dic = {1: 'data science', 2: 'Data Analytics'}
print(dic)
print(dic[1])
dic[1] = 'Data Mining'
print(dic)
dic[3] = 'Data Science'
print(dic)

# dic.clear()
# print(dic)

b=dic.copy()
print(b)

print(dic.values())
b={2:'Machine Learning'}
dic.update(b)
print(dic)

print(dic.get(2))
print(dic.keys())
print(dic.items())
print(dic.pop(3))
print(dic)
print(dic.popitem())
print(dic)

mydic=dict(key1='ML',key2='AI')
print(dict.fromkeys(mydic,'adsdf'))