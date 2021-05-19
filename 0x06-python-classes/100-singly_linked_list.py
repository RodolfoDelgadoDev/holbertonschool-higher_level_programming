#!/usr/bin/python3
""" Module Node """


class Node:

    """ Class Node  """

    def __init__(self, data, next_node=None):
        """ Contructor init """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Property data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter to data """
        if (type(value) != int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Property next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter to next_node """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

""" Module SinglyLinkedList """


class SinglyLinkedList:

    """ Class  SinglyLinkedList """

    def __init__(self):
        """ Contructor init """
        self.__head = None
        self.sorted_insert
        pass

    def __str__(self):
        """ Function to print the list """
        current_str = ""
        current_node = self.__head
        while (current_node is not None):
            current_str += (str(current_node.data))
            if (current_node.next_node is not None):
                current_str += "\n"
            current_node = current_node.next_node
        return current_str

    def sorted_insert(self, value):
        """ Function to insert in sort linked list """
        new_node = Node(value)
        current_node = self.__head
        if (current_node is None):
            self.__head = new_node
            return

        if (current_node.data > new_node.data):
            new_node.next_node = current_node
            self.__head = new_node
            return

        while(current_node.next_node is not None):
            if (current_node.next_node.data > new_node.data):
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
        current_node.next_node = new_node
