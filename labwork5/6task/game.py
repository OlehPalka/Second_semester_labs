"""
This module contains classes for game.
"""

monst_count = 0
list_of_gone_streets = list()


class Street:
    """
    this class creates streets in a game
    """

    def __init__(self, name: str):
        self.list_of_streets = list()
        self.name = name
        self.descr = ""
        self.character = None
        self.street_item = None

    def set_description(self, descr: str):
        """
        This method sets a description of the street.
        """
        self.descr = descr
        return descr

    def link_street(self, another_street: object, world_part: str):
        """
        this method sets streets conected with your`s.
        """
        self.list_of_streets.append(
            (another_street.name, world_part, another_street))
        return self.list_of_streets

    def get_details(self):
        """
        This method gives information about a street.
        """
        print(self.name)
        print("--------------------")
        print(self.set_description(self.descr))
        for i in self.list_of_streets:
            print(i[0] + " на " + i[1])
        if self.street_item != None:
            print("[" + self.street_item.name + "] тут - ", end="")
            print(self.street_item.describe())

    def move(self, command: str):
        """
        This method allows you to move to another street.
        """
        for i in self.list_of_streets:
            if command == i[1]:
                list_of_gone_streets.append(self)
                self = i[2]
        return self

    def return_gone_streets(self):
        return list_of_gone_streets

    def set_character(self, character: object):
        """
        This method sets an enemy to the street.
        """
        self.character = character

    def get_character(self):
        """
        This method returns enemy.
        """
        return self.character

    def set_item(self, item: object):
        """
        This method sets item to the street.
        """
        self.street_item = item

    def get_item(self):
        """
        This method returns item.
        """
        return self.street_item


class Enemy:
    """
    This class creates enemies.
    """

    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc
        self.given_item = None
        self.defeat = False

    def describe(self):
        """
        Enemy description.
        """
        print(self.name + " тут!")
        print(self.desc)
        if self.given_item != None:
            print(f"Ти маєш перемогти цього поганця, бо в нього є зброя, \
яку потрібно забрати, щоб перемогти фінального боса \
- {self.given_item.name}.")

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
        print("[" + self.name + " каже]: " + self.convers)

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

    def set_item(self, item):
        self.given_item = item


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
