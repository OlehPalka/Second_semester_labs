"""
This module contains classes which will help you to edit document.
"""


class Document:
    """
    This class allows you to control editing of a basic document.

    >>> doc = Document()
    >>> doc.filename = "test_document"
    >>> doc.filename
    'test_document'
    >>> doc.insert('h')
    >>> doc.insert('e')
    >>> doc.insert('l')
    >>> doc.insert('l')
    >>> doc.insert('o')
    >>> doc.save()
    >>> doc.string
    'hello'
    """

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        This method allows you to insert something to your file.

        >>> doc = Document()
        >>> doc.filename = "test_document"
        >>> doc.insert('h')
        >>> doc.insert('e')
        >>> doc.insert('l')
        >>> doc.insert('l')
        >>> doc.insert('o')
        >>> doc.string
        'hello'
        """
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        This method allows you to delete letter by moving cursor before it.
        An error will raise if you would like to delete impossible character.

        >>> doc = Document()
        >>> doc.filename = "test_document"
        >>> doc.insert('h')
        >>> doc.insert('e')
        >>> doc.insert('l')
        >>> doc.insert('l')
        >>> doc.insert('o')
        >>> doc.cursor.back()
        >>> doc.delete()
        >>> doc.string
        'hell'
        """
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            raise SymbolError("There is no symbol to delete.")

    def save(self):
        """
        THis method saves your file with given name.
        Saving without a name is impossible.
        In that case there will be an error.
        """
        if self.filename == '':
            raise NameError("The document you want to save hs no name!")
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        """
        This method returns symbols in file written together.

        >>> doc = Document()
        >>> doc.insert('h')
        >>> doc.insert('e')
        >>> doc.insert('y')
        >>> doc.string
        'hey'
        """
        return "".join((str(c) for c in self.characters))


class Cursor:
    """
    this class creates cursor, which helps you with navigating in file.

    >>> doc = Document()
    >>> curs = Cursor(doc)
    >>> curs.position
    0
    """

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """
        This method helps to move cursor forward in the file.
        If you try to move cursor over the file error will be raised.

        >>> doc = Document()
        >>> curs = Cursor(doc)
        >>> doc.insert('h')
        >>> doc.insert('e')
        >>> doc.insert('y')
        >>> curs.forward()
        >>> curs.position
        1
        """
        if self.position + 1 > len(doc.string):
            raise CursorError("Cursor went over the file")
        self.position += 1

    def back(self):
        """
        This method helps to move cursor back in the file.
        If you try to move cursor over the file error will be raised.

        >>> doc = Document()
        >>> curs = Cursor(doc)
        >>> doc.insert('h')
        >>> doc.insert('e')
        >>> doc.insert('y')
        >>> curs.forward()
        >>> curs.back()
        >>> curs.position
        0
        """
        if self.position - 1 < 0:
            raise CursorError("Cursor went over the file")
        self.position -= 1

    def home(self):
        """
        This method moves cursor to the beggining of the row.
        """
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        """
        This method moves cursor to the end of the row.
        """
        while self.position < len(self.document.characters) and self.document.characters[self.position].character != '\n':
            self.position += 1


class Character:
    """
    This class creates objects - stirng from your input.

    >>> char = Character("a")
    >>> char.character
    'a'
    """

    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        This method returns string from character.

        >>> char = Character("a")
        >>> char.__str__()
        'a'
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character


class CursorError(Exception):
    def __init__(self, text):
        self.text = text


class NameError(Exception):
    def __init__(self, text):
        self.text = text


class SymbolError(Exception):
    def __init__(self, text):
        self.text = text


if __name__ == "__main__":
    doc = Document()
    doc.filename = "test_document"
    doc.insert('h')
    doc.insert('e')
    doc.insert('l')
    doc.insert('l')
    doc.insert('o')
    print(doc.cursor.position)
    doc.cursor.back()
    doc.delete()
    doc.delete()
    doc.cursor.back()
    doc.cursor.back()
    doc.cursor.back()
    doc.cursor.back()
    doc.cursor.back()
    print(doc.string)
