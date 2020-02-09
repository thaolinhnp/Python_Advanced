from Class_Polygon import Polygon

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def ChuVi(self): # perimeter
        a,b,c = self.sides
        perimeter = a+b+c
        return perimeter
    def DienTich(self): #area
        a,b,c =  self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return area

if __name__ == "__main__":
    tri = Triangle()
    tri.input_sides()
    tri.display_sides()
    tri.ChuVi()
    tri.DienTich()
