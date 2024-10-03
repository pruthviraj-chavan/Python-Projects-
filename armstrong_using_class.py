class arm:
    def armstrong(self,n):
        p=len(str(n))
        s=0
        temp=n
        
        
        if n>0:
            while n!=0:
                r=n%10
                s=s+r**p
                n=n//10
            return temp==s
                
obj1=arm()
print(obj1.armstrong(int(input("n:"))))

        