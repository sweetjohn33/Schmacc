# A module to hold the different types of cards

from random import randint


class PermanentCard:

    # These are the permanent cards, including both monsters and buildings. They all have a bunch of stats
    # relevant to the game. We will keep track of their stats through "current" stats which will be modified as needed,
    # and "original" stats which will never change
    def __init__(self, name, health, defense, attack="", good_terrain="", bad_terrain="", owner=""):
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
        self._owner = owner

    def name(self) -> str:
        return self._name

    def set_owner(self, player):
        self._owner = player

    def owner(self):
        return self._owner

    def __repr__(self):
        return self._name

    def original_health(self):
        return self._Original_health

    def current_health(self):
        return self._Current_health

    def lose_health(self, health):
        self._Current_health -= health
        print(self.name() + " has lost " + str(health) + " health!")

    def original_defense(self):
        return self._Original_defense

    def current_defense(self):
        return self._Current_defense

    def original_attack(self):
        return self._Original_attack

    def current_attack(self):
        return self._Current_attack

    def check_land_compatibility(self, land):
        if land.name() == self._good_terrain:
            print(self._name + " is enjoying the " + land.name() + "! :)\n")
            self._Current_health += 1
            self._Current_attack += 1
            self._Current_defense += 1

        if land.name() == self._bad_terrain:
            print(self._name + " doesn't like the " + land.name() + " :(\n")
            self._Current_health -= 1
            self._Current_attack -= 1
            self._Current_defense -= 1
            if self._Current_health == 0:
                self.owner().send_to_graveyard(self)

    def return_to_original(self):
        self._Current_health = self._Original_health
        self._Current_defense = self._Original_defense
        self._Current_attack = self._Original_attack

    def combat(self, perm2, game):
        attack = self.current_attack() + randint(1, 12)
        defense = perm2.current_defense() + randint(1, 12)
        health_lost = attack - defense
        if health_lost >= 1:
            perm2.lose_health(health_lost)
        else:
            perm2.lose_health(1)
        if perm2.current_health() <= 0:
            print(perm2.name() + " Has been destroyed!")
            if perm2.card_class() == "Building":
                game.return_buildings().put_card_on_bottom(perm2)
                game.return_buildings().return_deck()[-1].return_to_original()
                found_already = 0
                while found_already == 0:
                    for building in perm2.owner().building_slots():
                        if building.name() == perm2.name() and building.current_health() == perm2.current_health():
                            building_index = perm2.owner().building_slots().index(building)
                            perm2.owner().lose_buildings(building_index)
                            found_already += 1


            else:
                perm2.owner().send_to_graveyard(perm2)
        else:
            print(perm2.name() + "'s health is now " + str(perm2.current_health()))


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
