n=int(input("n:"))

while len(str(n))>1:
    s=0
    temp=n
    while temp>0:
        s+=temp%10
        temp//=10
    n=s
print(n)
    
    