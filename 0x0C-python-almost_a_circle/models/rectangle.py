#!/usr/bin/python3
''' Module '''


from models.base import Base


class Rectangle(Base):
    ''' Rectangle using base '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    ''' property width '''

    @property
    def width(self):
        return self.__width

    ''' setter width '''

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    ''' property height '''

    @property
    def height(self):
        return self.__height

    ''' setter height '''

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    ''' property x '''

    @property
    def x(self):
        return self.__x

    ''' setter x '''

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    ''' property y '''

    @property
    def y(self):
        return self.__y

    ''' setter y '''

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    ''' area '''

    def area(self):
        return self.height * self.width

    ''' display '''

    def display(self):
        are = self.height * self.width
        c = 1
        sp = " " * self.x
        sal = "\n" * self.y
        print(sal, end="")
        print(sp, end="")
        for i in range(1, are + 1):
            if self.width * c == i:
                print("#")
                c += 1
                print(sp, end="")
            else:
                print("#", end="")

    ''' str '''

    def __str__(self):
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        e = self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    ''' update '''

    def update(self, *args):
        c = 1
        for i in args:
            if c == 1:
                self.id = i
                c += 1
                continue
            elif c == 2:
                self.width = i
                c += 1
                continue
            elif c == 3:
                self.height = i
                c += 1
                continue
            elif c == 4:
                self.x = i
                c += 1
                continue
            elif c == 5:
                self.y = i
                c += 1
                continue
