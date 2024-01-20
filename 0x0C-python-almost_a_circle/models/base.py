#!/usr/bin/python3

"""Module documentation for the Base class."""

class Base:
    """
    The Base class.

    Private class attribute:
        __nb_objects: Represents the number of objects created. Initialized to 0.

    Public instance attribute:
        id: Represents the identity of the object.

    Class constructor:
        __init__(self, id=None):
            If id is not None, assigns the public instance attribute id with this argument value.
            Otherwise, increments __nb_objects and assigns the new value to the public instance attribute id.
    """

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        If id is not None, assign the public instance attribute id with this argument value.
        Otherwise, increment __nb_objects and assign the new value to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


