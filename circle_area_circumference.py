class CIRCLE:
    
    def __init__(self,radius):
        self.radius=radius
        
        
    def area(self):
        a=3.14*self.radius*self.radius
        print(f"Area is {a}")
        
    def circumference(self):
        c=2*3.14*self.radius
        print(f"circumference is {c}")
        
a1=CIRCLE(int(input("enter radius")))
a1.area()
a1.circumference()