"""
Board module
"""


class Board:
    """
    Board creating class.
    """

    def __init__(self) -> None:
        self.current_position = [[' ', ' ', ' '],
                                 [' ', ' ', ' '],
                                 [' ', ' ', ' ']]
        self.last_move = ()

    def get_status(self):
        """
        Retutns status of the current board config.
        """
        for row in self.current_position:
            if row.count("x") == 3:
                return "x"
            if row.count("0") == 3:
                return "0"

        for col in range(3):
            if self.current_position[col][0] ==\
                    self.current_position[col][1] ==\
                    self.current_position[col][2] and self.current_position[col][0] != " ":
                return self.current_position[col][0]

        if self.current_position[0][0] == self.current_position[1][1] ==\
                self.current_position[2][2] or self.current_position[2][0] ==\
                self.current_position[1][1] == self.current_position[0][2] \
        and self.current_position[col][0] != " ":
            return self.current_position[1][1]

        empty = 0
        for row in range(3):
            for col in range(3):
                if self.current_position[row][col] == " ":
                    empty += 1

        if empty == 0:
            return "draw"

        return "continue"

    def make_move(self, position, turn):
        """
        This function makes move on the board.
        """
        if 0 <= position[0] <= 3 and 0 <= position[1] <= 3 and \
                self.current_position[position[0]][position[1]] == " ":
            self.current_position[position[0]][position[1]] = turn
        else:
            raise IndexError

    def possibilities(self):
        """
        returns all possible places on the board
        """
        result = []
        for row in range(3):
            for col in range(3):
                if self.current_position[row][col] == " ":
                    result.append((row, col))
        return result

    def make_computer_move(self):
        """
        This function makes computer move.
        """

    def __str__(self) -> str:
        result = ""
        for i in range(3):
            result += str(self.current_position[i]) + "\n"

        return result[:-1]
