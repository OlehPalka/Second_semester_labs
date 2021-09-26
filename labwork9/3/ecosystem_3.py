"""
Module with ecosystem
"""
import logging
import random
from animals_3 import Fish, Bear, Otter


class River:
    """
    Ecosistem class.
    """

    def __init__(self, size: int):
        self.size = size
        self.river_system = list()
        for _ in range(self.size):
            animal = random.choice([None, "F", "B", "O"])
            if animal is not None:
                gender = random.choice(["M", "F"])
                power = round(random.uniform(0.0, 100.0), 1)
                if animal == "F":
                    age = random.randint(0, 5)
                    self.river_system.append(Fish(gender, power, age))
                elif animal == "B":
                    age = random.randint(0, 10)
                    self.river_system.append(Bear(gender, power, age))
                else:
                    age = random.randint(0, 12)
                    self.river_system.append(Otter(gender, power, age))
            else:
                self.river_system.append(animal)

    def check_in_string(self):
        """
        This method returns string of animals, as the task requires.
        """
        # self.animal_population()
        result = list()
        for i in range(self.size):
            if self.river_system[i] is None:
                result.append("       ")
            else:
                if isinstance(self.river_system[i], Fish):
                    if self.river_system[i].age == 6:
                        self.river_system[i] = None
                        part = "       "
                    else:
                        part = self.river_system[i].letter + str(
                            (self.river_system[i].power, self.river_system[i].gender, self.river_system[i].age))
                        self.river_system[i].age += 1
                elif isinstance(self.river_system[i], Otter):
                    if self.river_system[i].age == 13:
                        self.river_system[i] = None
                        part = "       "
                    else:
                        part = self.river_system[i].letter + str(
                            (self.river_system[i].power, self.river_system[i].gender, self.river_system[i].age))
                        self.river_system[i].age += 1
                elif isinstance(self.river_system[i], Bear):
                    if self.river_system[i].age == 11:
                        self.river_system[i] = None
                        part = "       "
                    else:
                        part = self.river_system[i].letter + str(
                            (self.river_system[i].power, self.river_system[i].gender, self.river_system[i].age))
                        self.river_system[i].age += 1
                result.append(part)
        result = str(result)
        return result[1:-1]

    def animal_population(self):
        """
        Controls animal population.
        """
        list_of_animals = self.check()
        percent = 100 / self.size
        print(self.river_system)
        for i in ["B", "F", "O"]:
            if i == "B":
                clas = Bear
            elif i == "F":
                clas = Fish
            else:
                clas = Otter
            list_with_age = [
                (animal, animal.age) for animal in self.river_system if isinstance(animal, clas)]
            list_with_age.sort(key=lambda x: x[1])
            print(list_with_age)
            while list_of_animals.count(i) * percent > 60:
                self.river_system.remove(list_with_age[0][0])
                self.river_system.remove(list_with_age[-1][0])

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
                    self.birth(curent_animal, position, next_position)
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
            if isinstance(self.river_system[next_position], (Fish, Otter)):
                self.river_system[next_position] = curent_animal
                self.river_system[position] = None
                return "animal was killed"
            # перевірка на ведмедя в наступній клітині
            if isinstance(self.river_system[next_position], Bear):
                # перевірка на одну стать
                if self.river_system[next_position].gender != curent_animal.gender:
                    # додавання нової тварини
                    self.birth(curent_animal, position, next_position)
                else:
                    # ведмеді одної статі
                    if curent_animal.power < self.river_system[next_position].power:
                        self.river_system[position] = None
                    else:
                        self.river_system[next_position] = curent_animal
                        self.river_system[position] = None
                    return "a bear was killed"
        if isinstance(curent_animal, Otter):
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
                self.river_system[position] = None
                return "otter was killed"
            if isinstance(self.river_system[next_position], Otter):
                # перевірка на одну стать
                if self.river_system[next_position].gender != curent_animal.gender:
                    # додавання нової тварини
                    self.birth(curent_animal, position, next_position)
                else:
                    # видри одної статі
                    if curent_animal.power < self.river_system[next_position].power:
                        self.river_system[position] = None
                    else:
                        self.river_system[next_position] = curent_animal
                        self.river_system[position] = None
                    return "an otter was killed"

    def adding_animal(self, animal, position):
        """
        This method adds an animal to the ecosystem.
        """
        if self.river_system[position] is None:
            self.river_system[position] = animal
            return "animal was added"
        return "There already is an animal!"

    def birth(self, animal, position, next_position):
        """
        Method for giving birth of animal.
        """
        if isinstance(animal, Fish):
            children = 7
            gender = random.choice(["M", "F"])
            power = round(random.uniform(0.0, 100.0), 1)
            child = Fish(gender, power, 0)
        elif isinstance(animal, Otter):
            children = 3
            gender = random.choice(["M", "F"])
            power = round(random.uniform(0.0, 100.0), 1)
            child = Otter(gender, power, 0)
        elif isinstance(animal, Bear):
            children = 2
            gender = random.choice(["M", "F"])
            power = round(random.uniform(0.0, 100.0), 1)
            child = Bear(gender, power, 0)
        counter = 1
        while children != 0:
            try:
                if position-counter < 0 and next_position+counter > self.size - 1:
                    break
                if position-counter >= 0 and self.river_system[position-counter] is None:
                    self.adding_animal(child, position-counter)
                    children -= 1
                    if children == 0:
                        break
                if next_position+counter <= self.size and self.river_system[next_position+counter] is None:
                    self.adding_animal(child, next_position+counter)
                    children -= 1
                    if children == 0:
                        break
            except IndexError:
                break
            counter += 1

    def count_anim(self, animal):
        """
        This method counts setted animals in the ecosystem.
        """
        list_eco = self.check()
        return list_eco.count(animal)


if __name__ == "__main__":
    logging.basicConfig(filename='ecosystem_3.log', level=logging.INFO)
    river = River(12)
    logging.info(river.check_in_string())
    logging.info("Counting bears in the system.")
    logging.info(river.count_anim("B"))
    logging.info(river.check_in_string())
    logging.info("Adding bear to the first position")
    logging.info(river.adding_animal(Bear("M", 69.0, 9), 0))
    logging.info(river.check_in_string())
    logging.info("Moving animl from te first position to the second")
    logging.info(river.move_animal(0, 1))
    logging.info("Final system update.")
    logging.info(river.check_in_string())
