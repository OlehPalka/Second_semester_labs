from zip_processor import ZipProcessor
import sys
from PIL import Image


class ScaleZip(ZipProcessor):
    def __init__(self, zipname, shirina, visota):
        super().__init__(zipname)
        self.shirina = shirina
        self.visota = visota

    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((self.shirina, self.visota))
            scaled.save(str(filename))


if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4],
             zipname='photo_2020-05-13_14-21-32.zip', shirina=4000, visota=2000).process_zip()
