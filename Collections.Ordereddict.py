from collections import*;
N = int(input())
dic = OrderedDict()
for i in range(N):
    item = input().split()
    Price = int(item[-1])
    Name = " ".join(item[:-1])
    if(dic.get(Name)):
        dic[Name] += Price
    else:
        dic[Name] = Price
for i in dic.keys():
    print(i, dic[i])