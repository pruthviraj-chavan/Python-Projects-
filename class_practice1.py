class NUMBER:
    
    def __init__(self,n):
        self.n=n
        
    def even_odd(self):
        
        if self.n%2==0:
            print("it is even")
        else:
            print("its odd")
        
    def palindrome(self):
        
        s=0
        temp=abs(self.n)
        
        while self.n>0:
            r=self.n%10
            s=s+r
            self.n=self.n//10
        if temp==s:
            print("its palinndrome")
        else:
            print("not a palindrome")
            
        self.n=temp
            
    def factors(self):
        for i in range(1,self.n+1):
            if self.n%i==0:
                print(i,end=" ")
                
    def prime(self):
        c=0
        for i in range(1,self.n+1):
            if self.n%i==0:
                c+=1
        if c==2:
            print("prime")
        else:
            print("not pime")

            
    
            
            
e1=NUMBER(int(input("enter any number")))
e1.even_odd()
e1.palindrome()
e1.prime()
e1.factors()
