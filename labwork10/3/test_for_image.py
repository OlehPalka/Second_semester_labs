"""
Testing module for 3 lab task.
"""
import sys
from grayscaleimage import lzw_decompression, lzw_compression, from_file

image = "Зауваження 2021-04-13 184641.png"
print()
print()


if __name__ == "__main__":
    print(f"""The size of the image in the Array2D after decompression is {sys.getsizeof(
        lzw_decompression(lzw_compression(image), from_file(image).width(), from_file(image).height()))} bites""")

    print(
        f"""The size of original image in the Array2D is {sys.getsizeof(from_file(image))} bites""")

    print(
        f"""The size of the list after compression the image is {sys.getsizeof(lzw_compression(image))} bites""")
