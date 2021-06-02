#!/usr/bin/python3
'''MyInt'''


class MyInt(int):
    '''Square'''

    def __eq__(self, dis):
        return super().__ne__(dis)

    ''' ne '''
    def __ne__(self, dis):
        return super().__eq__(dis)
