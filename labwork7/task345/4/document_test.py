from document import Document, Cursor, Character

if __name__ == "__main__":
    doc = Document()
    doc.filename = "test_document"
    doc.insert('h')
    doc.insert('e')
    doc.insert('l')
    doc.insert('l')
    doc.insert('o')
    doc.cursor.back()
    doc.delete()
    doc.save()
    print(doc.string)
    curs = Cursor(doc)
    print(curs.position)
    curs.forward()
    print(curs.position)
    curs.back()
    print(curs.position)
    char = Character("a")
    print(char.character)
