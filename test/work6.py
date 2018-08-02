#1
'字符串练习'
'判断一个字符串，假设可以通过变换一个字母，使它变成回文字符串，也算是回文字符串'
'例如：123454721'
'通过把里面的7改成3，就变成了回文字符串'
'示例输入：123454721输出：True'
'示例输入：123454321输出：True'
'示例输入：103454721输出：False'
def is_need(a):
    flag=False
    count=0
    for i in range(a):
        if s[i]==s[-(i+1)]:
            pass
        else:
            count+=1
    if count<=1:
        flag=True
    return flag
s=input('请输入数字字符串：')
a=int(len(s)/2)
if len(s)%2==0:
    a=a+1
    print(is_need(a))
else:
    print(is_need(a))
#2
'多重循环的练习：' \
'求从0-9共10个数字，一共可以组合成多少个有效的3位数，并把全部结果输出'
for k in range(1,10):
    for i in range(10):
        for j in range(10):
            print(k*100+i*10+j)
#3
'现在有一个人，他可以一步跨1、2或3个阶梯，，求他从第0个阶梯到第10个阶梯的所有可能路线数量' 
'答案为：274种'
#n=1 1中 n=2 2种 n=3 4种 n>3时，n=(n-1)+(n-2)+(n-3)种
def num(n):#n为台阶数
    if n==3:
        return 4
    elif n==2:
        return 2
    elif n==1:
        return 1
    else:
        return num(n-1)+num(n-2)+num(n-3) 
print(num(10))


