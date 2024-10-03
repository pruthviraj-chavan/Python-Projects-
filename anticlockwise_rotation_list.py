''' n times rotation'''

l1=[1,2,3,4,5]
res=l1.pop(0)
l1.append(res)
print(l1)

'''by for loop'''

l2=[1,2,3,4,5]
n=int(input("n:"))
n=n%len(l2)

for i in range(n):
    temp=l2[0]
    for i in range(len(l2)-1):
        l2[i]=l2[i+1]
    l2[-1]=temp
print(l2)

