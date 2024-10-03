from abstract import CALCI

class CALCULATION(CALCI):
    def addition(self,*arg):
        return sum(arg)
    def difference(self,*arg):
        if len(arg)>0:
            res=arg[0]
            for i in range(1,len(arg)):
                res=arg[i]
            return res
        else:
            return "zero values given"