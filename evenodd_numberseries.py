n=int(input("n"))
for i in range(1,n+1):
    if i%2==0:
        print(i-1,end=" ")
    elif i%2!=0:
        print(i+1,end=" ")
