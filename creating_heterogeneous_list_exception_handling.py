n=int(input("n:"))
l1=[]

for i in range(1,n+1):
    val=input(i)
    try:
        l1.append(int(val))
    except:
        try:
            l1.append(float(val))
        except:
            try:
                l1.append(complex(val))
            except:
                l1.append(val)
print(l1)
    