class ONE:
    
    _a=100
    def __init__(self,p):
        self._p=p
    
    def meth(self):
        print("i am don")
        print(ONE._a)
        print(self._p)
        
obj=ONE(10)
obj.meth()

print(ONE._a) 
print(obj._p)