#!/usr/bin/python3
''' Module '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' init '''
        super().__init__(size, size, x, y, id)

    ''' __str__ '''

    def __str__(self):
        ''' str '''
        a = self.id
        b = self.x
        c = self.y
        d = self.size
        return "[Square] ({}) {}/{} - {}".format(a, b, c, d)

    ''' property setter '''

    @property
    def size(self):
        ''' size '''
        return self.width

    ''' setter propery '''

    @size.setter
    def size(self, value):
        ''' size '''
        self.width = value
        self.height = value
