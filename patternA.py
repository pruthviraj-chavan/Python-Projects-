n=int(input("n:"))
if n>=5:
    for i in range(n):
        for j in range(n-2):
            if i==0 or j==0 or i==n-2 or j==n-3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("enter greater than 5")