#An example of a class
class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    type = "Shape type not assigned yet"
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * self.width + 2 * self.length
    def describe(self, text):
        self.type = text
    def scaleSize(self, scale):
        self.width = self.width * scale
        self.length = self.length * scale
