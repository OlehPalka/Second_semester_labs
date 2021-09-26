"""
This module contains scaling photoes program.
"""

from pathlib import Path
import sys
from PIL import Image


class ScaleZip:
    """
    This class creates photoes and scales them
    """

    def __init__(self, zipname, width, height):
        self.width = width
        self.height = height
        self.temp_directory = Path("unzipped-{}".format(
            zipname[:-4]))

    def process_files(self):
        '''Scale each image in the directory'''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((self.width, self.height))
            scaled.save(str(filename))
