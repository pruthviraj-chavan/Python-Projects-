r = int(input())
c = int(input())
for i in range(r):
    val = c  
    for j in range(c):
        print(val, end=" ")
        val -= 1
    print()
