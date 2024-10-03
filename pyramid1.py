n=int(input("n"))
s=n-1
st=1
for i in range(n):
    for j in range(s):
        print(" ",end=" ")
    for k in range(st):
        print("*",end=" ")
    print()
    s-=1
    st+=2