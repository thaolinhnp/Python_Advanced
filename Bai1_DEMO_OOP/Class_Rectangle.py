from Class_Polygon import Polygon

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    def ChuVi(self):
        a,b = self.sides
        perimeter = (a+b)*2
        return perimeter
    def DienTich(self):
        a,b = self.sides
        area = a*b
        return area

if __name__ == "__main__":
    hcn = Rectangle()
    hcn.input_sides()
    hcn.display_sides()
    print('Chu vi: ',hcn.ChuVi())
    print('Dien tich:',hcn.DienTich())