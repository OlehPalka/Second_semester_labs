"""
This module contains two classes which creates objects (building and house).
"""


class Building:
    """
    This class creates buildings.

    >>> my_build = Building("koz_2a")
    >>> my_build.adress
    'koz_2a'
    """

    def __init__(self, adress):
        self.adress = adress


class Home(Building):
    """
    This class creeates objects (Home)
    """

    def __init__(self, adress, flats_list):
        super().__init__(adress)
        self.flats_list = flats_list


class Classroom:
    """
    This class creates objects of classroom type.

    >>> clasroom_016 = Classroom("016", 80, ['PC', 'projector', 'mic'])
    >>> clasroom_016.number
    '016'
    """

    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """
        This method conveerts inputed data to sentence.

        >>> clasroom_016 = Classroom("016", 80, ['PC', 'projector', 'mic'])
        >>> clasroom_016.__str__()
        'Classroom 016 has a capacity of 80 persons and has the following\
 equipment: PC, projector, mic.'
        """
        return "Classroom " + str(self.number) + " has a capacity of " + \
            str(self.capacity) + " persons and has the following equipment: "\
            + str(", ".join(self.equipment)) + "."

    def is_larger(self, second_classroom):
        """
        This function identyfies if the first room has bigger capacity.

        >>> clasroom_016 = Classroom("016", 80, ['PC', 'projector', 'mic'])
        >>> clas_2 = Classroom("2", 12, [])
        >>> clasroom_016.is_larger(clas_2)
        True
        """
        if self.capacity > second_classroom.capacity:
            return True
        return False

    def equipment_differences(self, second_classroom):
        """
        This function returns a list of items which are in the first room,
        but not in the second one.

        >>> clasroom_016 = Classroom("016", 80, ['PC', 'projector', 'mic'])
        >>> clas_2 = Classroom("2", 12, [])
        >>> clasroom_016.equipment_differences(clas_2)
        ['PC', 'projector', 'mic']
        """
        result = list()
        for i in self.equipment:
            if i not in second_classroom.equipment:
                result.append(i)
        return result

    def __repr__(self):
        """
        This function converts input data to sentence.

        >>> clasroom_016 = Classroom("016", 80, ['PC', 'projector', 'mic'])
        >>> clasroom_016.__repr__()
        "Classroom('016', 80, ['PC', 'projector', 'mic'])"
        """
        return "Classroom" + str((self.number, self.capacity, self.equipment))


class AcademicBuilding(Building):
    """
    This class generates objects of acadenic building type.
    """

    def __init__(self, adress, classrooms):
        super().__init__(adress)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        This function returns list of tuples of equipment and its number in classrooms.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> len(building.total_equipment())
        4
        """
        result = set()
        list_of_equipment = list()
        for equip in self.classrooms:
            for item in equip.equipment:
                list_of_equipment.append(item)
        for i in list_of_equipment:
            number_items = list_of_equipment.count(i)
            result.add((i, number_items))
        return list(result)

    def __str__(self):
        """
        This function prints information about building and classrooms.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building.__str__())
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector,\
 mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        result = str(self.adress)
        for i in self.classrooms:
            result += "\n" + str(i)
        return result
