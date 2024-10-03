def filter_five(n):
    return n%5==0
l1=[10,20,30,40,50,34,23,66]
res=[]
for i in l1:
    if filter_five(i):
        res.append(i)
print(res)