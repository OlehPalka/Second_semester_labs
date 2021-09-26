"""
This module contains function that checks if the board is
ready for the start of the game.
"""


import doctest


def horizontal_check(board):
    """
    This function checks horizontals in the board.

    >>> horizontal_check([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 6****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   2  **",\
    "  8  2***",\
    "  2  ****"\
    ])
    True
    """
    nums = "123456789 "
    for part in board:
        for element in part:
            if element not in nums and element not in "* ":
                return False
            if part.count(element) != 1 and element not in "* ":
                return False
    return True


def validate_board(board):
    """
    Function that founds if playground is ready for start of the game.

    >>> validate_board([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 6****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   2  **",\
    "  8  2***",\
    "  2  ****"\
    ])
    True
    >>> validate_board([\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"\
    ])
    False
    """
    nums = "123456789 "
    result = True
    result = horizontal_check(board)
    list_of_columns = list()
    for i in range(0, 8):
        part = ""
        for element in board:
            part += element[i]
        list_of_columns.append(part)
        for symbol in part:
            if symbol not in nums and symbol not in "* ":
                return False
            if symbol not in "* " and part.count(symbol) != 1:
                return False
    counter = 8
    final_board = list()
    for element in list_of_columns:
        element = element[:counter]
        final_board.append(element)
        counter -= 1
    for element in reversed(board):
        element = element[counter:]
        try:
            final_board[counter] += element
        except IndexError:
            final_board.append(element)
        counter += 1
    for part in final_board:
        for element in part:
            if element not in nums and element not in "* ":
                return False
            if part.count(element) != 1 and element not in "* ":
                return False
    return result


# print(doctest.testmod())
x = [i for i in range(10)]
print(x)
x.pop(0)
