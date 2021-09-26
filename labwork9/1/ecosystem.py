"""

"""
import logging
import random
import sys
from animals import *


class River:
    """
    Ecosistem class.
    """

    def __init__(self, size: int):
        self.size = size
        self.river_system = list()
        for _ in range(self.size):
            self.river_system.append(random.choice([None, Fish(), Bear()]))

    def check_in_string(self):
        """
        This method returns string of animals, as the task requires.
        """
        result = self.check()
        result = str(result)
        return result[1:-1]

    def check(self):
        """
        This method returns list of animals in the ecosystem.
        """
        result = list()
        for i in self.river_system:
            if i == None:
                result.append("N")
            else:
                result.append(i.letter)
        return result

    def move_animal(self, position, next_position):
        """
        This method does all the actions connected with moving of the animal.
        """
        try:
            curent_animal = self.river_system[position]
        except IndexError:
            print("Wrong animal position!")

        if abs(position - next_position) != 1 or next_position >= self.size:
            return "Impossible place chozen!"

        if curent_animal == None:
            return "It is not an animal!"

        if isinstance(curent_animal, Fish):
            if self.river_system[next_position] == None:
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
                return "animal was moved"
            elif isinstance(self.river_system[next_position], Bear):
                self.river_system[position] = None
            elif isinstance(self.river_system[next_position], Fish):
                if self.river_system[position-1] == None:
                    self.adding_animal(Fish(), position-1)
                    return "new fish was born"
                elif self.river_system[next_position+1] == None:
                    self.adding_animal(Fish(), next_position+1)
                    return "new fish was born"
        elif isinstance(curent_animal, Bear):
            if self.river_system[next_position] == None:
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
            elif isinstance(self.river_system[next_position], Fish):
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
            elif isinstance(self.river_system[next_position], Bear):
                if self.river_system[position-1] == None:
                    self.adding_animal(Bear(), position-1)
                    return "new bear was born"
                elif self.river_system[next_position+1] == None:
                    self.adding_animal(Bear(), next_position+1)
                    return "new bear was born"

    def adding_animal(self, animal, position):
        """
        This method adds an animal to the ecosystem.
        """
        if self.river_system[position] == None:
            self.river_system[position] = animal
        else:
            print("There already is an animal!")

    def count_anim(self, animal):
        """
        This method counts setted animals in the ecosystem.
        """
        list_eco = self.check()
        return list_eco.count(animal)


if __name__ == "__main__":
    logging.basicConfig(filename='ecosystem.log', level=logging.INFO)
    river = River(12)
    logging.info(river.check_in_string())
    logging.info("Counting bears in the system.")
    logging.info(river.count_anim("B"))
    logging.info(river.check_in_string())
    logging.info("Adding bear to the first position")
    logging.info(river.adding_animal(Bear(), 0))
    logging.info(river.check_in_string())
    logging.info("Moving animl from te first position to the second")
    logging.info(river.move_animal(0, 1))
    logging.info("Final system update.")
    logging.info(river.check_in_string())
