import abc
import math

class Shape(abc.ABC):
    @abc.abstractmethod
    def tinh_chu_vi(self):
        pass
    @abc.abstractmethod
    def tinh_dien_tich(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def tinh_chu_vi(self):
        return 2*math.pi*self.r
    def tinh_dien_tich(self):
        return math.pi * math.pow(self.r,2)

if __name__ == "__main__":
    cr = Circle(2)
    print(cr.tinh_chu_vi())