"""
This is module which contains two classes for cashing data from the webpage.
"""

import doctest
from datetime import datetime
from urllib.request import urlopen
from time import time

clean = open("date_note.txt", 'a')
clean_1 = open("cash_note.txt", 'a')
with open("date_note.txt") as file:
    if file.readlines() == []:
        with open("date_note.txt", 'w') as file:
            file.write("0000-00-00")


class Webpage_my:
    """
    This class creates object - chash webpage.
    This class works anyhow. As with ones defined object, as with different,
    as after closing of the program.

    >>> webpage = Webpage_my("https://www.fest.lviv.ua/uk/projects/uku/")
    >>> webpage.url
    'https://www.fest.lviv.ua/uk/projects/uku/'
    """

    def __init__(self, url):
        self.url = url
        self._content = None

    def rewriting_date_data(self, your_datetime):
        """
        This method rewrites date of your visit to webpage
        if it is bigger than previous.
        """
        with open("date_note.txt", 'w') as file:
            file.write(your_datetime)
        file.close()
        clean = open("cash_note.txt", 'w')
        clean.close()
        with open("cash_note.txt", 'w') as file:
            file.write(str(self._content))
        file.close()

    @property
    def content(self):
        """
        This method returns html webpage from webpage or from cashed file
        """
        with open("date_note.txt") as file:
            for i in file:
                date = i
        file.close()
        your_datetime = str(datetime.now())[:10]
        if your_datetime > date:
            if not self._content:
                print("Retrieving New Page...")
                self._content = urlopen(self.url).read()
                self.rewriting_date_data(your_datetime)
                return self._content
        else:
            with open("cash_note.txt") as file:
                return file.readlines()[0]


class WebPage:
    """
    This class creates object - chash webpage.
    This class works with only ones defined object.

    >>> webpage = WebPage("https://www.fest.lviv.ua/uk/projects/uku/")
    >>> webpage.url
    'https://www.fest.lviv.ua/uk/projects/uku/'
    """

    def __init__(self, url):
        self.url = url
        self._content = None
        self.your_date = str(datetime.now())[:10]

    @property
    def content(self):
        """
        This method returns content from webpage according to the visit time.
        """
        now_date = str(datetime.now())[:10]
        if not self._content or self.your_date < now_date:
            print("Getting from cache...")
            self._content = urlopen(self.url).read()
            self.your_date = now_date
        return self._content
