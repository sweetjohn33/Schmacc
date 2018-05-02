from random import randint


class PermanentCard:

    # These are the permanent cards, including both monsters and buildings. They all have a bunch of stats
    # relevant to the game. We will keep track of their stats through "current" stats which will be modified as needed,
    # and "original" stats which will never change
    def __init__(self, name, health, defense, attack="", good_terrain="", bad_terrain=""):
        """

        :param name: name of card
        :param health: original health of card
        :param defense: original defense
        :param attack: original attack
        :param good_terrain: card's preferred terrain
        :param bad_terrain: card's least preferred terrain
        """
        self._name = name
        self._Original_health = health
        self._Current_health = health
        self._Original_defense = defense
        self._Current_defense = defense
        self._Original_attack = attack
        self._Current_attack = attack
        self._good_terrain = good_terrain
        self._bad_terrain = bad_terrain

    def name(self) -> str:
        return self._name

    def original_health(self):
        return self._Original_health

    def current_health(self):
        return self._Current_health

    def original_defense(self):
        return self._Original_defense

    def current_defense(self):
        return self._Current_defense

    def original_attack(self):
        return self._Original_attack

    def current_attack(self):
        return self._Current_attack

    def return_to_original(self):
        self._Current_health = self._Original_health
        self._Current_defense = self._Original_defense
        self._Current_attack = self._Original_attack

    def __repr__(self):
        return self._name

    @staticmethod
    def combat(perm1, perm2):
        attack = perm1._attack + randint(1,12)
        defense = perm2._defense + randint(1,12)
        health_lost = attack - defense
        if health_lost >= 1:
            perm2._health -= health_lost
        else:
            perm2._health -= 1
        if perm2._health <= 0:
            print(perm2._name + " Has been destroyed!")
        else:
            print(perm2._name + "'s health is now " + str(perm2._health))


class BasicCreature(PermanentCard):
    def __init__(self, name, health, defense, attack="", good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Basic Creature"

    def card_class(self):
        return self._class


class NormalCreature(PermanentCard):
    def __init__(self, name, health, defense, attack="", good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Normal Creature"

    def card_class(self):
        return self._class


class EliteCreature(PermanentCard):
    def __init__(self, name, health, defense, attack="", good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Elite Creature"


class Building(PermanentCard):
    def __init__(self, name, health, defense, attack="", good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Building"

    def card_class(self):
        return self._class

# We have subclasses for eah type of permanent card where the only difference between the types is their "class" which
# is basically just what tier of monster it is


class Spell:
    # Spells will essentially defined by their name only,they have no other attributes so far... however, eventually
    # subtypes of spell card may be added

    def __init__(self, name):
        """

        :param name: name of spell
        """
        self._name = name

    def name(self) -> str:
        return self._name

    def __repr__(self):
        return self._name

    def __str__(self):
        return self.__repr__()
