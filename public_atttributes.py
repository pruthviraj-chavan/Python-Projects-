class ONE:
    
    a=100
    def __init__(self,p):
        self.p=p
    
    def meth(self):
        print("i am don")
        print(ONE.a)
        print(self.p)
        
obj=ONE(10)
obj.meth()

print(ONE.a)
print(obj.p)