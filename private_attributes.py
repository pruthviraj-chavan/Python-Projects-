class ONE:
    
    __a=100
    def __init__(self,p):
        self.__p=p
    
    def meth(self):
        print("i am don")
        print(ONE.__a)
        print(self.__p)
        
obj=ONE(10)
obj.meth()

'''print(ONE._a) #attribute error
print(obj._p) #attribute error'''