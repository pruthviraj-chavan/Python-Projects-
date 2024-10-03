n=int(input("n:"))

l=[]
sum=0
for i in range(1,n):
    if n%i==0:
        l.append(i)
        
print(l,end=" ")
        
for  i in range(len(l)):
    if l[i]==n:
        break
    sum=sum+l[i]
if sum==n:
    print("perfect")
    
else:
    print("not perfect")
   
    
print(sum,end=" ")