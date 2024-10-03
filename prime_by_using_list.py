l=[]
n=int(input("n:"))

for i in range(1,n+1):
    if n%i==0:
        l.append(i)
        
if len(l)==2:
    print("is a prime")
else:
    print("not a prime")