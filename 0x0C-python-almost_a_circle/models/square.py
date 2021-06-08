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
                    self.size = i
                    c += 1
                elif c == 3:
                    self.x = i
                    c += 1
                elif c == 4:
                    self.y = i
                    c += 1
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    ''' to dictonary '''

    def to_dictionary(self):
        ''' dictonary '''
        a = self.id
        b = self.size
        c = self.x
        d = self.y
        return {'id': a, 'size': b, 'x': c, 'y': d}
