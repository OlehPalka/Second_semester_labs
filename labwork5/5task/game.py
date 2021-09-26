"""
This module contains classes for game.
"""
monst_count = 0


class Room:
    """
    this class creates rooms in a game
    """

    def __init__(self, name: str):
        self.list_of_rooms = list()
        self.name = name
        self.descr = ""
        self.character = None
        self.room_item = None

    def set_description(self, descr: str):
        """
        This method sets a description of the room.
        """
        self.descr = descr
        return descr

    def link_room(self, another_room: object, world_part: str):
        """
        this method sets rooms conected with your`s.
        """
        self.list_of_rooms.append(
            (another_room.name, world_part, another_room))
        return self.list_of_rooms

    def get_details(self):
        """
        This method gives information about room.
        """
        print(self.name)
        print("--------------------")
        print(self.set_description(self.descr))
        for i in self.list_of_rooms:
            print("The " + i[0] + " is " + i[1])
        if self.room_item != None:
            print("The [" + self.room_item.name + "] is here - ", end="")
            print(self.room_item.describe())

    def move(self, command: str):
        """
        This method allows you to movw to another room.
        """
        for i in self.list_of_rooms:
            if command == i[1]:
                self = i[2]
        return self

    def set_character(self, character: object):
        """
        This method sets an enemy to the room.
        """
        self.character = character

    def get_character(self):
        """
        This method returns enemy.
        """
        return self.character

    def set_item(self, item: object):
        """
        This method sets item to the room.
        """
        self.room_item = item

    def get_item(self):
        """
        This method returns item.
        """
        return self.room_item


class Enemy:
    """
    This class creates enemies.
    """

    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc
        self.defeat = False

    def describe(self):
        """
        Enemy description.
        """
        print(self.name + " is here!")
        print(self.desc)

    def set_conversation(self, convers):
        """
        This method sets conversation.
        """
        self.convers = convers

    def set_weakness(self, weak):
        """
        This method sets enemies weakness.
        """
        self.weak = weak

    def talk(self):
        """
        This method prints setted talk.
        """
        print("[" + self.name + " says]: " + self.convers)

    def fight(self, weapon):
        """
        This method returns a result of the fight.
        """
        if weapon == self.weak:
            self.defeat = True
            return self.defeat

    def get_defeated(self):
        """
        This method returns a number of defeated enemies.
        """
        global monst_count
        monst_count += 1
        return monst_count


class Item:
    """
    This class cretes room items
    """

    def __init__(self, name):
        self.name = name

    def set_description(self, descr):
        """
        Item description.
        """
        self.descr = descr

    def describe(self):
        """
        Returns item description.
        """
        return self.descr

    def get_name(self):
        """
        returns item name.
        """
        return self.name
