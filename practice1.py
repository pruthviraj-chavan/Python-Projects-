n=int(input("n"))
v=1
s=ord('A')
for i in range(n):
  
    
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        if i&1==0:
            print(v,end=" ")
        else:
            print(chr(s),end=" ")
    print()
    if i&1==0:
        v+=1
    else:
        s+=1
        
      