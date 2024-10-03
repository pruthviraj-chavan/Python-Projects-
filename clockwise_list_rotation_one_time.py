l1=[1,2,3,4,5]
res=l1.pop()
l1.insert(0,res)
print(l1)

'''without function'''
l2=[1,2,3,4,5]
temp=l2[-1]
for i in range(len(l2)-1,0,-1):
    l2[i]=l2[i-1]
l2[0]=temp
print(l2)
    
'''by using slicing'''

l3=[1,2,3,4,5]
m=int(input("m:"))
m=m%len(l1)
for i  in range(m):
    
    l3=[l3[len(l3)-1:]+l3[:len(l3)-1]]
print(l3)

    