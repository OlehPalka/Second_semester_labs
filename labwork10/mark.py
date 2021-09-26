"""
This module contains class which saves data in array
"""
import ctypes


class AngleADT:
    """
    Class which creates object (array) which saves angles.
    """

    def __init__(self):
        self.ascii = {'0': 0.0, '1': 22.5, '2': 45.0, '3': 67.5,
                      '4': 90.0, '5': 112.5, '6': 135.0, '7': 157.5,
                      '8': 180.0, '9': 202.5, 'a': 225.0, 'b': 247.5,
                      'c': 270.0, 'd': 292.5, 'e': 315.0, 'f': 337.5}

    def word_lenth(self):
        """
        This method counts lenth of the future array
        """
        result = 0
        for i in self.message:
            result += len(hex(ord(i))) - 2
        return result

    def encode_message(self, message):
        """
        This is encoding method.
        """
        self.message = message
        lenth = self.word_lenth()
        result = Array(lenth)
        encoded_mes = "".join([hex(ord(i))[2:] for i in self.message])
        for i in range(lenth):
            if i > 0:
                if prevoius_char == encoded_mes[i]:
                    angle = 360.0
                else:
                    angle = self.ascii[encoded_mes[i]] - \
                        self.ascii[prevoius_char]
                result[i] = angle
            else:
                result[i] = self.ascii[encoded_mes[i]]
            prevoius_char = encoded_mes[i]
        return result

    def print_array(self, array):
        """
        This is printing method.
        """
        result = list()
        for i in range(self.word_lenth()):
            result.append(array[i])
        print(result)


# Implements the Array ADT using array capabilities of the ctypes module.


class Array:
    """
    Creates an array with size elements.
    """

    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__(self):
        """
        Returns the size of the array.
        """
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        """
        Gets the contents of the index element.
        """
        assert len(self) > index >= 0, "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        """
        assert len(self) > index >= 0, "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value):
        """
        Clears the array by setting each element to the given value.
        """
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        """
        return _ArrayIterator(self._elements)

# An iterator for the Array ADT.


class _ArrayIterator:
    """
    Array iterator
    """

    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        raise StopIteration


x = AngleADT()
x.encode_message('1 січня')
x.print_array(x.encode_message("1 січня"))
