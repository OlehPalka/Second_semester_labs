"""
Module with ecosystem
"""
import logging
import random
from animals_2 import Fish, Bear


class River:
    """
    Ecosistem class.
    """

    def __init__(self, size: int):
        self.size = size
        self.river_system = list()
        for _ in range(self.size):
            animal = random.choice([None, "F", "B"])
            if animal is not None:
                gender = random.choice(["M", "F"])
                power = round(random.uniform(0.0, 100.0), 1)
                if animal == "F":
                    self.river_system.append(Fish(gender, power))
                else:
                    self.river_system.append(Bear(gender, power))
            else:
                self.river_system.append(animal)

    def check_in_string(self):
        """
        This method returns string of animals, as the task requires.
        """
        result = list()
        for i in self.river_system:
            if i is None:
                result.append("       ")
            else:
                part = i.letter + str((i.power, i.gender))
                result.append(part)
        result = str(result)
        return result[1:-1]

    def check(self):
        """
        This method returns list of animals in the ecosystem.
        """
        result = list()
        for i in self.river_system:
            if i is None:
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
            return "Wrong animal position!"

        if abs(position - next_position) != 1 or next_position >= self.size:
            return "Impossible place chozen!"

        if curent_animal is None:
            return "It is not an animal!"
        # перевірка для риб
        if isinstance(curent_animal, Fish):
            # переміщення
            if self.river_system[next_position] is None:
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
                return "animal was moved"
            # перевірка на наявність ведмедя у наступній позиції
            if isinstance(self.river_system[next_position], Bear):
                self.river_system[position] = None
                return "fish was killed"
            # перевірка на рибу у наступній позиції
            if isinstance(self.river_system[next_position], Fish):
                # перевірка на протилежну стать для народжування нової особи
                if self.river_system[next_position].gender != curent_animal.gender:
                    if self.river_system[position-1] is None and position-1 != -1:
                        gender = random.choice(["M", "F"])
                        power = round(random.uniform(0.0, 100.0), 1)
                        self.adding_animal(Fish(gender, power), position-1)
                        return "new fish was born"
                    if self.river_system[next_position+1] is None:
                        gender = random.choice(["M", "F"])
                        power = round(random.uniform(0.0, 100.0), 1)
                        self.adding_animal(
                            Fish(gender, power), next_position+1)
                        return "new fish was born"
                else:
                    # одна стать - вбивство однієї тварини
                    if curent_animal.power < self.river_system[next_position].power:
                        self.river_system[position] = None
                    else:
                        self.river_system[next_position] = curent_animal
                        self.river_system[position] = None
                    return "fish was killed"
        # перевірка на ведмедя
        if isinstance(curent_animal, Bear):
            # переміщення
            if self.river_system[next_position] is None:
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
                return "animal was moved"
            # перевірка на рибу в наступній клітині
            if isinstance(self.river_system[next_position], Fish):
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
                return "fish was killed"
            # перевірка на ведмедя в наступній клітині
            if isinstance(self.river_system[next_position], Bear):
                # перевірка на одну стать
                if self.river_system[next_position].gender != curent_animal.gender:
                    # додавання нової тварини
                    if self.river_system[position-1] is None:
                        gender = random.choice(["M", "F"])
                        power = round(random.uniform(0.0, 100.0), 1)
                        self.adding_animal(Bear(gender, power), position-1)
                        return "new bear was born"
                    if self.river_system[next_position+1] is None:
                        gender = random.choice(["M", "F"])
                        power = round(random.uniform(0.0, 100.0), 1)
                        self.adding_animal(
                            Bear(gender, power), next_position+1)
                        return "new bear was born"
                else:
                    # ведмеді одної статі
                    if curent_animal.power < self.river_system[next_position].power:
                        self.river_system[position] = None
                    else:
                        self.river_system[next_position] = curent_animal
                        self.river_system[position] = None
                    return "a bear was killed"

    def adding_animal(self, animal, position):
        """
        This method adds an animal to the ecosystem.
        """
        if self.river_system[position] is None:
            self.river_system[position] = animal
            return "animal was added"
        return "There already is an animal!"

    def count_anim(self, animal):
        """
        This method counts setted animals in the ecosystem.
        """
        list_eco = self.check()
        return list_eco.count(animal)


if __name__ == "__main__":
    logging.basicConfig(filename='ecosystem_2.log', level=logging.INFO)
    river = River(12)
    logging.info(river.check_in_string())
    logging.info("Counting bears in the system.")
    logging.info(river.count_anim("B"))
    logging.info(river.check_in_string())
    logging.info("Adding bear to the first position")
    logging.info(river.adding_animal(Bear("M", 69.0), 0))
    logging.info(river.check_in_string())
    logging.info("Moving animl from te first position to the second")
    logging.info(river.move_animal(0, 1))
    logging.info("Final system update.")
    logging.info(river.check_in_string())
