"""
This module contains class which makes operation with photoes
and text files.
"""


import shutil
import zipfile
from pathlib import Path
from scale_zip import ScaleZip
from zip_replace import ZipReplace


class ZipProcessor:
    """
    This class creates object - file and makes chosen operations with it.
    """

    def __init__(self, zipname, width=0, height=0, search_string="", replace_string=""):
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(
            zipname[:-4]))
        self.width = width
        self.height = height
        self.search_string = search_string
        self.replace_string = replace_string
        self.scale_zip = ScaleZip(
            self.zipname, self.width, self.height)
        self.zip_replace = ZipReplace(
            self.zipname, self.search_string, self.replace_string)

    def process_zip(self):
        """
        This method makes unzipping processing and zipping.
        """
        self.unzip_files()
        if self.width != 0:
            self.scale_zip.process_files()
            self.temp_directory = self.scale_zip.temp_directory
        else:
            self.zip_replace.process_files()
            self.temp_directory = self.zip_replace.temp_directory
        self.zip_files()

    def unzip_files(self):
        """
        This method unzips files
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        This method zips file back
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))
