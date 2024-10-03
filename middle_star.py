n=int(input("n:"))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1 or (j==n-3 and i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    