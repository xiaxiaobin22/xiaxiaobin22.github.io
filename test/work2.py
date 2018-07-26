#1
a = 100
b = 'I love python deep in my heart'
c = 90.00
print('Do you love python?{0}.please give a mark to python. Not {1} but {2}~!'.format(b,c,a))
#2
x=0
l1 = [1,2,3,4]
l2 = [2,3,4,5]
l3=list()
list1=zip(l1,l2)
for i in list1:
    l3.append(sum(i))
print(l3)
#3
l1 = [1,2,3,4,5,6,7]
def change(l1):
    for i in range(0,len(l1),2):
        x=l1[i]
        l1[i]=l1[i+1]
        l1[i+1]=x
if len(l1)%2==0:
    change(l1)
else:
    rest=l1[-1]
    l1=l1[:-1]
    change(l1)
    l1.append(rest)
print(l1)

#4
f1 = open('D:/file/my way.txt',"r",encoding='utf-8')
f2 = open('D:/file/my way 英文.txt',"a",encoding='utf-8')
f3 = open('D:/file/my way 中文.txt',"a",encoding='utf-8')
def is_alphabet(uchar):
        """判断一个unicode是否是英文字母"""
        if (uchar >= u'\u0041' and uchar<=u'\u005a') \
        or (uchar >= u'\u0061' and uchar<=u'\u007a'):
                return True
        else:
                return False
def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False
for line in f1:
    line=line.strip()
    if is_alphabet(line):
        f2.write(line)+'\n'
    elif is_chinese(line):
        f3.write(line)
f1.close()
f2.close()
f3.close()