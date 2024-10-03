n=int(input("n:"))

bin=0
p=1
while n>0:
    
    rem=n%2
    bin=bin+rem*p
    n=n//2
    p*=10
    
    
    
print(bin)
    