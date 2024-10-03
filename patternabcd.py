n=int(input("n:"))
val=ord('A')
for i in range(n):
    for j in range(n):
        print(chr(val),end=' ')
        val+=1
        if val>ord('Z'):
            val=ord('A')
    print()
    val-=1