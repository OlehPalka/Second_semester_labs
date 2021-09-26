"""
This is a testing module for file cache_webpage.py
"""

import cache_webpage
from time import time
if __name__ == "__main__":
    webpage = cache_webpage.WebPage("http://www.blankwebsite.com/")
    now = time()
    content1 = webpage.content
    print(time() - now)
    now = time()
    content2 = webpage.content
    print(time() - now)
    print(content1 == content2)
    print()
    webpage = cache_webpage.Webpage_my("http://www.blankwebsite.com/")
    now = time()
    content1 = webpage.content
    print(time() - now)
    now = time()
    content2 = webpage.content
    print(time() - now)
    print(content1 == content2)
