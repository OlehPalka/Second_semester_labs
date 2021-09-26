"""
This module contains program which works with photoes.
"""
from io import StringIO
from PIL import Image, ImageOps
from arrays import Array2D


class GrayscaleImage:
    """
    This class turns color photo to black and white.
    """

    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.photo = Array2D(nrows, ncols)
        self.configure(0)

    def configure(self, value):
        """
        Configures the grid to contain the given live cells.

        :param coord_list:
        :return:
        """
        for rows in range(self.photo.num_rows()):
            for col in range(self.photo.num_cols()):
                self.photo.__setitem__((rows, col), value)

    def width(self):
        """
        Returns width of the picture.
        """
        return self.photo.num_rows()

    def height(self):
        """
        Returns height of the picture.
        """
        return self.photo.num_cols()

    def clear(self, value):
        """
        Cleares the grid.
        """
        while value < 0 or value > 255:
            print("You have entered wrong value.")
            value = input("Reenter the value: ")
        self.configure(value)

    def getitem(self, row, col):
        """
        Reurns the item by given indexes
        """
        while row < 0 or row > self.nrows or col < 0 or col > self.ncols:
            print("You have entered wrong values for rows and cols.")
            row = input("Reenter the row: ")
            col = input("Reenter the col: ")
        return self.photo[row, col]

    def setitem(self, row, col, value):
        """
        Sets the item by given indexes
        """
        while row < 0 or row > self.nrows or col < 0 or col > self.ncols:
            print("You have entered wrong values for rows and cols.")
            row = input("Reenter the row: ")
            col = input("Reenter the col: ")
        while value < 0 or value > 255:
            print("You have entered wrong value.")
            value = input("Reenter the value: ")
        self.photo[row, col] = value


def from_file(path):
    """
    Creates object GrayscaleImage from the path to the file.
    """
    # creating a image object
    image = Image.open(f"{path}")

    # creating greyscale image object by applying greyscale method
    image_grayscale = ImageOps.grayscale(image)

    # size of image
    size = image_grayscale.size
    photo = GrayscaleImage(size[0], size[1])
    pixels = image_grayscale.load()
    for row in range(size[0]):
        for col in range(size[1]):
            photo.setitem(row, col, pixels[row, col])
    return photo


def lzw_compression(path: str):
    """
    This function compress the image from the given path.
    """
    letters = ""
    intention = from_file(path)
    for row in range(intention.width()):
        for col in range(intention.height()):
            letters += chr(intention.getitem(row, col))

    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    enc_str = ""
    result = []
    for i in letters:
        cur_chr = enc_str + i
        if cur_chr in dictionary:
            enc_str = cur_chr
        else:
            result.append(dictionary[enc_str])
            dictionary[cur_chr] = dict_size
            dict_size += 1
            enc_str = i
    if enc_str:
        result.append(dictionary[enc_str])
    return result


def lzw_decompression(data_list: list, nrows: int, ncols: int):
    """
    Decompress a list of output ks to a string.
    """
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    result = StringIO()
    enc_str = chr(data_list.pop(0))
    result.write(enc_str)
    for i in data_list:
        if i in dictionary:
            entry = dictionary[i]
        elif i == dict_size:
            entry = enc_str + enc_str[0]
        else:
            raise ValueError('Bad compressed k: %s' % i)
        result.write(entry)
        dictionary[dict_size] = enc_str + entry[0]
        dict_size += 1

        enc_str = entry
    result = result.getvalue()
    photo = GrayscaleImage(nrows, ncols)
    counter = 0
    for row in range(nrows):
        for col in range(ncols):
            photo.setitem(row, col, ord(result[counter]))
            counter += 1
    return photo
