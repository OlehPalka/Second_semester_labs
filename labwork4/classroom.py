"""
This module contains Class and methods connected with classrooms.
"""


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


if __name__ == "__main__":
    clasroom_016 = Classroom("016", 80, ['PC', 'projector', 'mic'])
    clas_2 = Classroom("2", 12, [])
    print(clasroom_016.is_larger(clas_2))
