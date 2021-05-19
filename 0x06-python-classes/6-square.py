#!/usr/bin/python3
'''Class Square'''


class Square():
    '''size validation'''

    def __init__(self, size=0, position=(0, 0)):
        check = isinstance(size, (int))
        ent1 = isinstance(position[0], int)
        ent2 = isinstance(position[1], int)
        if check is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        tu = isinstance(position, (tuple))
        if tu is False or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (ent1 is False) or (ent2 is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    '''check area of a square'''

    def area(self):
        self.ar = self.__size ** 2
        return self.ar
    '''def retrive size'''

    @property
    def size(self):
        return self.__size

    '''def setter size'''

    @size.setter
    def size(self, value):
        check = isinstance(value, (int))
        if check is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    '''def my_print'''

    def my_print(self):
        a = self.__size ** 2
        c = 1
        s = self.__position[0] * " "
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for i in range(1, a + 1):
                if i == 1:
                    print(s, end="")
                if i == self.__size * c:
                    if i == a:
                        print("#")
                    else:
                        print("#")
                        print(s, end="")
                        c += 1
                else:
                    print("#", end="")

    ''' def retrive position'''

    @property
    def position(self):
        return self.__position

    ''' def setter position '''

    @position.setter
    def position(self, value):
        tu = isinstance(value, (tuple))
        ent1 = isinstance(value[1], (int))
        entr2 = isinstance(value[0], (int))
        if tu is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif entr1 is False or entr2 is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
