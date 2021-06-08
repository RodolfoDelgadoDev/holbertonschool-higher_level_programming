#!/usr/bin/python3
''' Module '''


from models.base import Base


class Rectangle(Base):
    ''' Rectangle using base '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' init '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    ''' property width '''

    @property
    def width(self):
        ''' width '''
        return self.__width

    ''' setter width '''

    @width.setter
    def width(self, value):
        ''' width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    ''' property height '''

    @property
    def height(self):
        ''' height '''
        return self.__height

    ''' setter height '''

    @height.setter
    def height(self, value):
        ''' height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    ''' property x '''

    @property
    def x(self):
        ''' x '''
        return self.__x

    ''' setter x '''

    @x.setter
    def x(self, value):
        ''' x '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    ''' property y '''

    @property
    def y(self):
        ''' y '''
        return self.__y

    ''' setter y '''

    @y.setter
    def y(self, value):
        ''' y '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    ''' area '''

    def area(self):
        ''' area '''
        return self.height * self.width

    ''' display '''

    def display(self):
        ''' display '''
        are = self.height * self.width
        c = 1
        sal = "\n" * self.y
        print(sal, end="")
        sp = " " * self.x
        print(sp, end="")
        for i in range(1, are + 1):
            if self.width * c == i:
                print("#")
                c += 1
                if i != are:
                    print(sp, end="")
            else:
                print("#", end="")

    ''' str '''

    def __str__(self):
        ''' __str__ '''
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        e = self.height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    ''' update '''

    def update(self, *args, **kwargs):
        ''' update '''
        c = 1
        if args:
            for i in args:
                if c == 1:
                    self.id = i
                    c += 1
                elif c == 2:
                    self.width = i
                    c += 1
                elif c == 3:
                    self.height = i
                    c += 1
                elif c == 4:
                    self.x = i
                    c += 1
                elif c == 5:
                    self.y = i
                    c += 1
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

