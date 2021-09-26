"""
This module contain class which replaces text in file.
"""

from pathlib import Path
import sys
import os


class ZipReplace:
    """
    This class creates text file and makes replacing in it.
    """

    def __init__(self, zipname, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(
            zipname[:-4]))

    def process_files(self):
        '''perform a search and replace on all files in the
        temporary directory'''
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
        contents = contents.replace(self.search_string, self.replace_string)
        with filename.open("w") as file:
            file.write(contents)
