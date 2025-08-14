class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x=(self.coor2[0] - self.coor1[0])**2
        y=(self.coor2[1] - self.coor1[1])**2
        result=(x+y)**0.5
        return result
    
    def slope(self):
        x=self.coor2[0] - self.coor1[0]
        y=self.coor2[1] - self.coor1[1]
        result=y/x
        return result

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())