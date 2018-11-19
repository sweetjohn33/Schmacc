# A module to hold the different types of cards


class Card:

    # These are the permanent cards, including both monsters and buildings. They all have a bunch of stats
    # relevant to the game. We will keep track of their stats through "current" stats which will be modified as needed,
    # and "original" stats which will never change

    def __init__(self, name, effect):
        """

        :param name:
        :param health:
        :param defense:
        :param attack:
        :param good_terrain:
        :param bad_terrain:
        :param trigger:
        :param effect: A dictionary of the following format: { "effect_function1(" : [trigger, [type_of_object,
                       what_players, what_zone, how_many_targets], effect_counter, effect_function2 : ...}

        """
        self.name = name
        self.effect = effect




class BasicCreature(Card):
    def __init__(self, name, effect, health, defense, attack, good_terrain="", bad_terrain=""):
        super().__init__(name, effect)
        self.type = "Basic Creature"
        self.original_health = health
        self.current_health = health
        self.original_defense = defense
        self.current_defense = defense
        self.original_attack = attack
        self.current_attack = attack
        self.good_terrain = good_terrain
        self.bad_terrain = bad_terrain
        self.owner = None
        self.land = None
        self.previous_land = None

    def cardtype(self):
        return self.type


class NormalCreature(Card):
    def __init__(self, name, effect, health, defense, attack, good_terrain="", bad_terrain=""):
        super().__init__(name, effect)
        self.type = "Normal Creature"
        self.original_health = health
        self.current_health = health
        self.original_defense = defense
        self.current_defense = defense
        self.original_attack = attack
        self.current_attack = attack
        self.good_terrain = good_terrain
        self.bad_terrain = bad_terrain
        self.owner = None
        self.land = None
        self.previous_land = None



class EliteCreature(Card):
    def __init__(self, name, effect, health, defense, attack, good_terrain="", bad_terrain=""):
        super().__init__(name, effect)
        self.type = "Elite Creature"
        self.original_health = health
        self.current_health = health
        self.original_defense = defense
        self.current_defense = defense
        self.original_attack = attack
        self.current_attack = attack
        self.good_terrain = good_terrain
        self.bad_terrain = bad_terrain
        self.owner = None
        self.land = None
        self.previous_land = None




class Building(Card):
    def __init__(self, name, effect, health, defense):
        super().__init__(name, effect)
        self.type = "Building"
        self.original_health = health
        self.current_health = health
        self.original_defense = defense
        self.current_defense = defense
        self.owner = None




# We have subclasses for each type of permanent card where the only difference between the types is their "class" which
# is basically just what tier of monster it is


class Spell(Card):
    # Spells will essentially defined by their name only,they have no other attributes so far... however, eventually
    # subtypes of spell card may be added

    def __init__(self, name, effect):
        super().__init__(name, effect)
        self.name = name
        self.effect = effect
        self.type = "Spell"

    def __repr__(self):
        return self.name

    def name(self):
        print(self.name)


    # def play_card(self, =None):
    #     if  is None:
    #         exec(self._effect)
    #

