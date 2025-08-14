class Cylinder:
    
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        result = Cylinder.pi*self.radius*self.radius*self.height
        return result
    
    def surface_area(self):
        result1 = 2*Cylinder.pi*self.radius*self.height
        result2 = 2*Cylinder.pi*self.radius*self.radius
        result = result1+result2
        return result

c = Cylinder(2,3)
print(f"{c.volume():1.2f}")
print(f"{c.surface_area():1.1f}")