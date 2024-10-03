#153 1cube+5cube+3cube = 153

n=int(input("n:"))
s=0
p=0
temp=abs(n)

for i in range(1,n+1):
   
    if n>0:
        while n!=0:
            r=n%10
            s=s+(r*r*r)
            
            n=n//10
            
            
            
            
if s==temp:
    print("armstrong number")
else:
    print("not a armstrong number")
    
            