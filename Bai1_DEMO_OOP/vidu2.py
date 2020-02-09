class vector():
    def __init__(self,a,b):
        self.__a = a
        self.b = b

    def __str__(self):
        return 'vector (%d,%d)' % (self.__a, self.b)

    def __add__(self,other):
        return vector(self.__a + other.__a,self.b + other.b)

if __name__ == "__main__":
    vector1 = vector(1,3)
    print(vector1)
    vector2 = vector(3,4)
    print(vector2)
    vector3 = vector1 + vector2
    print(vector3)
    print(vector.__a)
