#day3 and day4 1(1)

import math 
L1 = [53, 40, 10, 37, 91, 97, 87, 45, 15, 12, 29, 21, 73, 77, 91, 55, 46, 64, 37, 29]
print(sum(L1)/len(L1))
#1(2)
L1 = [53, 40, 10, 37, 91, 97, 87, 45, 15, 12, 29, 21, 73, 77, 91, 55, 46, 64, 37, 29]
L1.sort()
L1=L1[1:-1]
a=round(sum(L1)/len(L1)/10)
print(a)
#2
s = 'he9llowo5rldIlo2vepy7thon'
list1=list(s)
string=''
for i in list1:
    if i.isdigit():
        string=string+i
print(int(string))
#day4 1
def is_num():
    while True:
        flag=False
        a=input('请输入字符串:')
        b=int(len(a)/2)
        if len(a)%2!=0:
            if a[:b]==a[-1:b:-1]:
                flag=True
        else:
            if a[:b]==a[-1:b-1:-1]:
                flag=True
        print(flag)
is_num()
#2
string=input('请输入字符串:')
location=int(input('请输入开始位置'))
string=string[location-1:]+string[:location-1]
print(string)
#3
list1=list()
count1=0
count2=0
count3=0
f1=open('log.txt','r',encoding='UTF-8')
for i in f1:
    list1.append(i.split())
for i in list1:
    if i[0].find('.jpeg')!=-1:
        count1=count1+int(i[1])
    elif i[0].find('.json')!=-1:
        count2=count2+int(i[1])
    elif i[0].find('.png')!=-1:
        count3=count3+int(i[1])
print(count1,count2,count3)
#4
dict1={
    1001:{'name':'小皮','分数':89},
    1002:{'name':'小猪','分数':97},
    1003:{'name':'小哈','分数':66}
      }
list1=[]
for i in dict1.keys():
    list1.append(dict1[i])
a=sorted(list1,key=lambda x:x['分数'],reverse=True)
for j in a:
    print(j['name'])