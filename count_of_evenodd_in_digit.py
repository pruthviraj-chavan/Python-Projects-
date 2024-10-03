n=int(input("n:"))
zc,oc,ec=0,0,0


while(n!=0):
    r=n%10
    if r==0:
        zc+=1
    elif r%2==0:
        ec+=1
    else:
        oc+=1
    n=n//10
print(zc,oc,ec, sep="\n")
    