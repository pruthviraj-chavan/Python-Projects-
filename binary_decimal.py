n=int(input("n:"))
p=1
dec=0
while n>0:
    
    rem=n%10
    dec=dec+rem*p
    n//=10
    p*=2
print(dec)
    