# A module to hold the different types of cards

from random import randint
from Game_Function.Triggers import Trigger


class PermanentCard:

    # These are the permanent cards, including both monsters and buildings. They all have a bunch of stats
    # relevant to the game. We will keep track of their stats through "current" stats which will be modified as needed,
    # and "original" stats which will never change

    def __init__(self, name, effect, health, defense, attack=0, good_terrain="", bad_terrain="", 
                 targets=""):
        """

        :param name:
        :param health:
        :param defense:
        :param attack:
        :param good_terrain:
        :param bad_terrain:
        :param trigger:
        :param effect:
        :param targets: a list of the following format: [object type, zone, players, number]
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
        print("\n" + self.name() + " has lost " + str(health) + " health!\n")

    def original_defense(self):
        return self._Original_defense

    def current_defense(self):
        return self._Current_defense

    def original_attack(self):
        return self._Original_attack

    def current_attack(self):
        return self._Current_attack

    def return_effect(self):
        return self._effect

    def trigger_check(self, number):
        check = Trigger(number)
        for trigger in self._trigger:
            if trigger == check:
                return True
        return False

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
        attack_roll = randint(1, 12)
        defense_roll = randint(1, 12)
        print(self._name + " Has rolled a " + str(attack_roll) + "!\n")
        print(perm2.name() + " Has rolled a " + str(defense_roll) + "!\n")
        attack = self.current_attack() + attack_roll
        defense = perm2.current_defense() + defense_roll
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
                perm2.previous_land().delete_monster()
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
                        print(str(buildings.index(building) + 1) + ") " + building.name() + ": Health: " +
                              str(building.current_health()) + "  |||  Defense: " + str(building.current_defense()))
                    new_target = input("What is your next victim?\n")
                new_target = int(new_target) - 1
                self.combat(buildings[new_target], game)
            elif perm2.previous_land().monster_slot().name() == "DJ Meow Mix":
                print("DJ Meow Mix is in big trouble...")
                self.combat(perm2.previous_land().monster_slot(), game)
            else:
                print("Your " + self.name() + "has totally cleared this column out bro, good work.")

        else:
            print("\n" + perm2.name() + "'s health is now " + str(perm2.current_health()) + "\n")
        self.land_switch(self._previous_land)

    def pick_target(self, effect, game):
        if effect
        viable_players = []
        viable_targets = []
        if self._target[2] == "all":
            for player in game.return_players().return_deck():
                viable_players.append(player)
        if self._target[2] == "opponents":
            for player in game.return_players().return_deck():
                if player.name() != self._owner.name():
                    viable_players.append(player)
        if self._target[2] == "owner":
            for player in game.return_players().return_deck():
                if player.name() == self._owner.name():
                    viable_players.append(player)
        if self._target[0] == "creature":
            if self._target[1] == "graveyard":
                for player in viable_players:
                    for monster in player.graveyard():
                        viable_targets.append(monster)

            if self._target[1] == "battlefield":
                for player in viable_players:
                    for land in player.lands():
                        for monster in land.monster_slot():
                            viable_targets.append(monster)

        if self._target[0] == "building":
            for player in viable_players:
                for land in player.lands():
                    for building in land.building_slots():
                        viable_targets.append(building)
        if self._target[0] == "player":
            for player in viable_players:
                viable_targets.append(player)
        chosen_targets = []
        for i in range(self._target[4]):
            for g in range(len(viable_targets)):
                print(str(g + 1) + ") " + viable_targets[g].owner().name() + ": " + viable_targets[g].name())
            target = input("Which card would you like to target?")
            target = int(target) - 1
            chosen_targets.append(viable_targets[target])
            del viable_targets[target]

        effect = self._effect + str(chosen_targets) + ")"
        return effect





class BasicCreature(PermanentCard):
    def __init__(self, name, effect, health, defense, attack, good_terrain="", bad_terrain="", 
                 targets=""):
        super().__init__(name, effect, health, defense, attack, good_terrain, bad_terrain, 
                 targets)
        self._class = "Basic Creature"

    def card_class(self):
        return self._class


class NormalCreature(PermanentCard):
    def __init__(self, name, effect, health, defense, attack, good_terrain="", bad_terrain="", 
                 targets=""):
        super().__init__(name, effect, health, defense, attack, good_terrain, bad_terrain, 
                 targets)
        self._class = "Normal Creature"

    def card_class(self):
        return self._class


class EliteCreature(PermanentCard):
    def __init__(self, name, effect, health, defense, attack, good_terrain="", bad_terrain="", 
                 targets=""):
        super().__init__(name, effect, health, defense, attack, good_terrain, bad_terrain,  
                 targets)
        self._class = "Elite Creature"

    def card_class(self):
        return self._class

class Building(PermanentCard):
    def __init__(self, name, effect, health, defense, attack=0, good_terrain="", bad_terrain="", 
                 targets=""):
        super().__init__(name, effect, health, defense, attack, good_terrain, bad_terrain, 
                 targets)
        self._class = "Building"

    def card_class(self):
        return self._class

    def total_boost(self, boost):
        self._Current_health += boost
        self._Current_defense += boost

    def land_switch(self, land):
        self._previous_land = self._land
        self._land = land

# We have subclasses for each type of permanent card where the only difference between the types is their "class" which
# is basically just what tier of monster it is


class Spell(PermanentCard):
    # Spells will essentially defined by their name only,they have no other attributes so far... however, eventually
    # subtypes of spell card may be added

    def __init__(self, name, effect, health=0, defense=0, attack=0, good_terrain="", bad_terrain="", 
                 targets=""):
        super().__init__(name, effect, health, defense, attack, good_terrain, bad_terrain,  
                         targets)
        self._class = "Spell"

    def card_class(self):
        return self._class

    # def play_card(self, targets=None):
    #     if targets is None:
    #         exec(self._effect)
    #

