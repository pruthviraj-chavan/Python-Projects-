l1=eval(input("enter list"))
c=input("enter character")[0].lower()
res=list(filter(lambda n:n[0]==c,l1))
print(res)