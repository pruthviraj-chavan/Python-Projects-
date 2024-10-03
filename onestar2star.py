n=int(input("n"))
v=1
for i in range(n):
    for j in range(n):
    
        print(v,end=" ")
        
    if v<n:
        print()
     
        print("* "*n,end=" ")   
    print()
    v+=1
    if v>9:
        v=1
        
        