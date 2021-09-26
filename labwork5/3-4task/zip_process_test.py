import scale_zip
import sys
if __name__ == "__main__":
    smth = scale_zip.ScaleZip(*sys.argv[1:4],
                              zipname='oleh_palka_lab5.zip', shirina=1000, visota=1000).process_zip()
    smth_1 = scale_zip.ScaleZip(*sys.argv[1:4],
                                zipname='oleh_palka_lab5.zip', shirina=1000, visota=1000).process_zip()
    print(smth == smth_1)
