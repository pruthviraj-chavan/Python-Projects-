n=int(input("n"))
sum=0

if n>0:
    while(n!=0):
        r=n%10
        sum+=r
        n=n//10
    print(sum)
elif n<0:
    while(n!=0):
        n=abs(n)
        r=n%10
        sum+=r
        n=n//10
    print(sum)
else:
    print("not a number")
    