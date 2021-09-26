"""
This module contains class building and it`s methods.
"""
import classroom


class AcademicBuilding:
    """
    This class makes operations with imported class classroom,
    and inputed iformation.
    """

    def __init__(self, address, classrooms):
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        """
        This function returns list of tuples of equipment and its number in classrooms.

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
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

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building.__str__())
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector,\
 mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        result = str(self.address)
        for i in self.classrooms:
            result += "\n" + str(i)
        return result


if __name__ == "__main__":
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    classrooms_1 = [classroom_016, classroom_007, classroom_008]
    building = AcademicBuilding('Kozelnytska st. 2a', classrooms_1)
