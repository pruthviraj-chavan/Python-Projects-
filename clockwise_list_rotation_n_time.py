''' n times rotation'''

l1=[1,2,3,4,5]
n=int(input("n:"))
n=n%len(l1)
for i in range(n):
    temp=l1[-1]
    for i in range(len(l1)-1,0,-1):
        l1[i]=l1[i-1]
    l1[0]=temp
print(l1)