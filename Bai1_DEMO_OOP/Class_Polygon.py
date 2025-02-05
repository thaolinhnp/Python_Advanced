class Polygon():
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def input_sides(self):
        self.sides = [float(input('Enter side'+str(i+1)+':')) for i in range(self.number_of_sides)]

    def display_sides(self):
        for i in range(self.number_of_sides):
            print('Side',i+1,'is',self.sides[i])

if __name__ == "__main__":
    pol = Polygon(3)
    pol.input_sides()
    pol.display_sides()