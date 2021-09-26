from zip_processor import ZipProcessor
import sys
if __name__ == "__main__":
    zipname = input("Please, enter file name for replacing: ")
    search_string = input("Please, enter searched string: ")
    replace_string = input("Please, enter replaced string: ")
    smth = ZipProcessor(*sys.argv[1:4],
                        zipname,  search_string=search_string, replace_string=replace_string)

    smth.process_zip()
    smth = smth.zip_replace

    zipname = input("Please, enter file name for scaling: ")
    width = input("Please, enter width: ")
    height = input("Please, enter height: ")
    smth_1 = ZipProcessor(*sys.argv[1:4],
                          zipname, width=width, height=height)
