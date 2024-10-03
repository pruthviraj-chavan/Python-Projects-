n=int(input("n:"))
s=1

while(n!=0):
    
        r=n%10
        if r!=0:
            s*=r
        n=n//10
print(s)