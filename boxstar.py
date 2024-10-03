n=int(input("n:"))
v=1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print(v,end=" ")
            v+=1
            if v>9:
                v=1
        else:
            print(" ",end=" ")
    print()   