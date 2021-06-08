#!/usr/bin/python3
''' Module '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' init '''
        super().__init__(size, size, x, y, id)
        self.size = size

    ''' __str__ '''
    def __str__(self):
        ''' str '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
