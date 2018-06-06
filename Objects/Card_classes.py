# A module to hold the different types of cards

from random import randint
from Objects.Triggers import Trigger


class PermanentCard:

    # These are the permanent cards, including both monsters and buildings. They all have a bunch of stats
    # relevant to the game. We will keep track of their stats through "current" stats which will be modified as needed,
    # and "original" stats which will never change

    def __init__(self, name, health, defense, attack=0, good_terrain="", bad_terrain="", trigger=0, effect=""):
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
        self._owner = None
        self._land = None
        self._previous_land = None
        self._trigger = Trigger(trigger)
        self._effect = effect

    def name(self) -> str:
        return self._name

    def set_owner(self, player):
        self._owner = player

    def owner(self):
        return self._owner

    def __repr__(self):
        return self._name

    def __str__(self):
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

    def return_trig(self):
        return self._Trigger

    def total_boost(self, boost):
        self._Current_health += boost
        self._Current_attack += boost
        self._Current_defense += boost

    def land(self):
        return self._land

    def previous_land(self):
        return self._previous_land

    def land_switch(self, land):
        self._previous_land = self._land
        self._land = land
        if self._previous_land is not None:
            if self._previous_land.name() == self._good_terrain:
                self.total_boost(-1)
            if self._previous_land.name() == self._bad_terrain:
                self.total_boost(1)
        if self._land is not None:
            if self._land.name() == self._good_terrain:
                self.total_boost(1)
                print(self.owner().name() + "'s " + self.name() + " is boosted in the " + self._land.name())
            if self._land.name() == self._bad_terrain:
                self.total_boost(-1)
        if self._land is None:
            self.return_to_original()

    def good_land(self):
        return self._good_terrain

    def return_to_original(self):
        self._Current_health = self._Original_health
        self._Current_defense = self._Original_defense
        self._Current_attack = self._Original_attack

    def combat(self, perm2, game):
        self.land_switch(perm2.land())
        if self._Current_health <= 0:
            print(self.name() + "has been destroyed before the battle has even begun! What a wimp.")
            self.return_to_original()
            self._owner.send_to_graveyard(self)
            self._land.delete_monster()
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
                perm2.return_to_original()
                perm2.owner().send_to_graveyard(perm2)
                perm2.land().delete_monster()
            buildings = perm2.previous_land().building_slots()
            if len(buildings) > 0:
                new_target = ""
                tried_before = 0
                while not new_target.isdigit() or int(new_target) - 1 not in \
                        range(len(buildings)):
                    if tried_before > 0:
                        print("Invalid Input, try again.")
                    print(self.name() + " is on a rampage! What else would you like to attack?")
                    for building in buildings:
                        print(str(buildings.index(building) + 1) + ") " + building + ": Health: " +
                              str(building.current_health()) + "|||  Defense: " + str(building.current_defense()))
                    new_target = input("What is your next victim?")
                new_target = int(new_target) - 1
                self.combat(buildings[new_target], game)
            elif perm2.previous_land().monster_slot().name() == "DJ Meow Mix":
                print("DJ Meow Mix is in big trouble...")
                self.combat(perm2.previous_land().monster_slot(), game)
            else:
                print("Your " + self.name() + "has totally cleared this column out bro, good work.")

        else:
            print(perm2.name() + "'s health is now " + str(perm2.current_health()))
        self.land_switch(self._previous_land)


class BasicCreature(PermanentCard):
    def __init__(self, name, health, defense, attack, good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Basic Creature"

    def card_class(self):
        return self._class


class NormalCreature(PermanentCard):
    def __init__(self, name, health, defense, attack, good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Normal Creature"

    def card_class(self):
        return self._class


class EliteCreature(PermanentCard):
    def __init__(self, name, health, defense, attack, good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Elite Creature"


class Building(PermanentCard):
    def __init__(self, name, health, defense, attack=0, good_terrain="", bad_terrain=""):
        super().__init__(name, health, defense, attack, good_terrain, bad_terrain)
        self._class = "Building"

    def card_class(self):
        return self._class

    def total_boost(self, boost):
        self._Current_health += boost
        self._Current_defense += boost

    def land_switch(self, land):
        self._previous_land = self._land
        self._land = land

# We have subclasses for eah type of permanent card where the only difference between the types is their "class" which
# is basically just what tier of monster it is


class Spell:
    # Spells will essentially defined by their name only,they have no other attributes so far... however, eventually
    # subtypes of spell card may be added

    def __init__(self, name, trigger=0, effect=""):
        """

        :param name: name of spell
        """
        self._name = name
        self._trigger = Trigger(trigger)
        self._effect = effect

    def name(self) -> str:
        return self._name

    def __repr__(self):
        return self._name

    def __str__(self):
        return self.__repr__()

    def play_card(self, targets=None):
        if targets is None:
            exec(self._effect)
