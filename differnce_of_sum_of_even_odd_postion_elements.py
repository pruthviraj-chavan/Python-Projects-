n=int(input("n"))
l1=eval(input("values"))[:n]

even=0
odd=0


for i in range(len(l1)):
    if i%2!=0:
        even+=l1[i]
    elif i%2==0:
        odd+=l1[i]
        
difference=even-odd
print(difference)
        
''' or

n=int(input("n))
l1=eval(input("values"))[:n]
res=sum(l1[::2])-sum(l1[1::2])
print(res)'''