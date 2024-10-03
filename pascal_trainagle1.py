n=int(input("n:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    val=1
    for k in range(i+1):
        print(val,end=" ")
        val= val * (i-k) // (k+1)
    print()
    