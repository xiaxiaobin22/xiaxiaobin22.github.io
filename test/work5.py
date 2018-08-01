'''将下面的列表按下列形式转换成字典' \
'例如：[('A',1),('B',2),('C',3)]
转换成的字典 {'A':1,'B':2,'C':3}
要求将计算过程写成函数的形式,函数的返回值是转换后形成的字典
'''
#1
L = [('小花',97),('小皮',89),('小小',67),('小滴',86),('小布',54)]
#方法一：
def list_to_dict1(L):
    dic=dict()
    for i in L:
        dic[i[0]]=i[1]
    return dic
print(list_to_dict1(L))
#方法二
def list_to_dict2(L):
    dic=dict(L)
    return dic
print(list_to_dict2(L))
#2
'制作一个大小写字母的ASCII对照表，每行输出4个字母及其ASCII' 
'做出如下输出：' 
'a:97   b:98    c:99    d:100' 
'xx     xx      xx      xx  ' 
'xx     xx      xx      xx'
def lower(a):
    string=''
    for i in range(26):
        key=chr(a+i)
        value=ord(key)
        string=string+key+':'+str(value)+'\t'
        if (i+1)%4==0:
            string=string+'\n' 
    return string 
print(lower(97))
print(lower(65))
#3
'计算列表中重复最多次的数字' 
'例如：[1,9,6,6,7,9,6,1,2]' 
'应该输出:6   3' 
'6为重复最多的数字，3为次数'
data = [42, 57, 79, 59, 27, 87, 66, 72, 39, 5, 19, 4, 54, 51, 98, 46, 65, 45, 9, 7,
        53, 64, 53, 50, 10, 98, 42, 94, 34, 26, 29, 96, 83, 23, 69, 70, 1, 18, 62, 33,
        8, 71, 38, 83, 46, 62, 33, 79, 67, 81, 26, 79, 36, 67, 63, 71, 95, 88, 45, 81,
        45, 99, 8, 29, 78, 32, 92, 67, 71, 94, 39, 5, 43, 61, 84, 78, 37, 31, 57, 101,
        23, 71, 16, 85, 41, 16, 95, 80, 15, 51, 39, 32, 38, 72, 71, 62, 49, 49, 13, 45]
for i in range(1,len(data)):
    max_num=data[0]
    max_count=data.count(data[0])
    if data.count(data[i]>max_num):
        max_num=data[i]
        max_count=data.count(data[i])
print(max_num,max_count)



