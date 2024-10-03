n=int(input("n"))
l1=eval(input("values"))[:n]
res=0
for i in  l1:
    if i%2!=0:
        res+=i 
print(res)