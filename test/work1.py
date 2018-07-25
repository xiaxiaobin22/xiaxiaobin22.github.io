#1
l1 = [1,2,3,4] 
l2 = [5,6,7,8]
list1=list()
l3=[] 
for i in range(len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
print(l3)
#2
l1 = [1,2,3,4] 
l2 = [5,6,7,8]
list1=list()
l1=l1[::-1]
l2=l2[::-1]
l3=[] 
for i in range(len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
print(l3)
#3
score = {'小花':89,'小白':67,'小小':56,'小灰':79,'小哈':97,'小皮':86,'小马':77}
list1=list()
for i,j in score.items():
    list1.append([j,i])
list1.sort(reverse=True)
for item in range(3):
    print(list1[item][1])