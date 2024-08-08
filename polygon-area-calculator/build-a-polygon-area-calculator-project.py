class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        wh = ', '.join(f"{i}={getattr(self, i)}" for i in vars(self))
        return f"{self.__class__.__name__}({wh})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        return_str = ''
        if self.height < 50 and self.width < 50:
            for height in range(self.height):
                return_str += '*' * self.width
                return_str += '\n'
            return return_str
        return 'Too big for picture.'

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.side})"

    def  set_side(self,side):
        self.side = side 
        super().set_width(self.side)
        super().set_height(self.side)

    def set_width(self, width):
        self.side = width
        super().set_width(self.side)
        super().set_height(self.side)
    
    def set_height(self, height):
        self.side = height
        super().set_width(self.side)
        super().set_height(self.side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))