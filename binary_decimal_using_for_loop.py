n=int(input("n:"))

dec=0

p=len(str(n))-1

for i in str(n):
    dec=dec+int(i)*(2**p)
    
    p-=1
print(dec)