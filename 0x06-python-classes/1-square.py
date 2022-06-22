"""
Write a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """The blueprint for all instances"""

    def __init__(self, size):
        """Initialize a private instance attribute"""

        self.__size = size
    pass


"""
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module

Why?

Why size is private attribute?

The size of a square is crucial for a square,
many things depend of it (area computation, etc.),
so you, as class builder, must control the type and value of this attribute.
One way to have the control is to keep it privately.
You will see in next tasks how to get,
update and validate the size value.
"""
