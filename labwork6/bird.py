# class Bird:

#     def __init__(self, name):
#         self.name = name
#         self.eggs = []

#     def __repr__(self):
#         if len(self.eggs) == 1:
#             return f"{self.name} has {len(self.eggs)} egg"
#         return f"{self.name} has {len(self.eggs)} eggs"

#     def count_eggs(self):
#         return len(self.eggs)

#     def get_eggs(self):
#         return self.eggs.copy()

#     def fly(self):
#         return "I can fly!"

#     def lay_egg(self):
#         self.eggs.append(Egg())


class Egg:
    def __str__(self):
        return "egg"


# class Penguin(Bird):
#     def fly(self):
#         return "No flying for me."

#     def swim(self):
#         return "I can swim!"


# class MessengerBird(Bird):
#     def __init__(self, name, message=None):
#         self.message = message
#         super().__init__(name)

#     def deliver_message(self):
#         if self.message != None:
#             return self.message
#         return ""


# def get_local_methods(clss):
#     import types
#     # This is a helper function for the test function below.
#     # It returns a sorted list of the names of the methods
#     # defined in a class. It's okay if you don't fully understand it!
#     result = []
#     for var in clss.__dict__:
#         val = clss.__dict__[var]
#         if (isinstance(val, types.FunctionType)):
#             result.append(var)
#     return sorted(result)


# def test_bird_classes():
#     print("Testing Bird classes...", end="")
#     # A basic Bird has a species name, can fly, and can lay eggs
#     bird1 = Bird("Parrot")
#     assert (type(bird1) == Bird)
#     assert (isinstance(bird1, Bird))
#     assert (bird1.fly() == "I can fly!")
#     assert (bird1.count_eggs() == 0)
#     assert (str(bird1) == "Parrot has 0 eggs")

#     # here changes
#     assert (bird1.lay_egg() is None)
#     eggs = bird1.get_eggs()
#     egg = eggs.pop()
#     assert (type(egg) == Egg)
#     assert (isinstance(egg, Egg))
#     # here changes ends

#     assert (bird1.count_eggs() == 1)
#     assert (str(bird1) == "Parrot has 1 egg")
#     bird1.lay_egg()
#     assert (bird1.count_eggs() == 2)
#     assert (str(bird1) == "Parrot has 2 eggs")
#     assert (get_local_methods(Bird) == [
#             '__init__', '__repr__', 'count_eggs', 'fly', 'get_eggs', 'lay_egg'])

#     # A Penguin is a Bird that cannot fly, but can swim
#     bird2 = Penguin("Emperor Penguin")
#     assert (type(bird2) == Penguin)
#     assert (isinstance(bird2, Penguin))
#     assert (isinstance(bird2, Bird))
#     assert (bird2.fly() == "No flying for me.")
#     assert (bird2.swim() == "I can swim!")
#     bird2.lay_egg()
#     assert (bird2.count_eggs() == 1)
#     assert (str(bird2) == "Emperor Penguin has 1 egg")
#     assert (get_local_methods(Penguin) == ['fly', 'swim'])

#     # A MessengerBird is a Bird that can optionally carry a message
#     bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
#     assert (type(bird3) == MessengerBird)
#     assert (isinstance(bird3, MessengerBird))
#     assert (isinstance(bird3, Bird))
#     assert (not isinstance(bird3, Penguin))
#     assert (bird3.deliver_message() == "Top-Secret Message!")
#     assert (str(bird3) == "War Pigeon has 0 eggs")
#     assert (bird3.fly() == "I can fly!")

#     bird4 = MessengerBird("Homing Pigeon")
#     assert (bird4.deliver_message() == "")
#     bird4.lay_egg()
#     assert (bird4.count_eggs() == 1)
#     assert (get_local_methods(MessengerBird)
#             == ['__init__', 'deliver_message'])
#     print("Done!")


class Book:
    def __init__(self, name, author, current_page, ):

    def get_current_page()


def test_book_class():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone",
                 "J. K. Rowling", 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert (str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
            "1 page, currently on page 1>")

    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turn_page(4)  # turning pages does not return
    assert (book1.get_current_page() == 5)
    book1.turn_page(-1)
    assert (book1.get_current_page() == 4)
    book1.turn_page(400)
    assert (book1.get_current_page() == 309)
    assert (str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
            "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turn_page(-1)
    assert (book2.get_current_page() == 1)
    book2.turn_page(1)
    assert (book2.get_current_page() == 1)

    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " +
            "662 pages, currently on page 1>")
    assert (book3.get_bookmarked_page() == None)
    book3.turn_page(9)
    book3.place_bookmark()  # does not return
    assert (book3.get_bookmarked_page() == 10)
    book3.turn_page(7)
    assert (book3.get_bookmarked_page() == 10)
    assert (book3.get_current_page() == 17)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " +
            "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turn_to_bookmark()
    assert (book3.get_current_page() == 10)
    book3.remove_bookmark()
    assert (book3.get_bookmarked_page() == None)
    book3.turn_page(25)
    assert (book3.get_current_page() == 35)
    book3.turn_to_bookmark()  # if there's no bookmark, don't turn to a page
    assert (book3.get_current_page() == 35)
    assert (str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " +
            "662 pages, currently on page 35>")

    # Finally, you should be able to compare two books directly
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    assert (book5 == book6)
    assert (book5 != book7)
    assert (book5 != book8)
    book5.turn_page(1)
    assert (book5 != book6)
    book5.turn_page(-1)
    assert (book5 == book6)
    book6.place_bookmark()
    assert (book5 != book6)
    print("Done!")
