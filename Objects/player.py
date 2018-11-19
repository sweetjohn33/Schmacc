# A module to hold the player class
from random import randint
from Objects.Land import Land
from Objects.Card_classes import PermanentCard
from Objects.Card_classes import Spell


class Player:

    # Here is our player. He has a name, a count of neutered rabbits and food, and lists of all his assets.
    # These include mainly his lands, his spells, and his graveyard. The building and monster list is used mainly
    # to start the game, as the player receives all of his monsters/buildings in a list and decides in what order to
    # place them, instead of receiving and placing the monsters/buildings one at a time

    def __init__(self, name="player"):
        """

        :param name: the name of the player
        """
        self.name = name
        self.neutered_rabbits = 0
        self.graveyard = []
        self.spells = []
        self.buildings = []
        self.creatures = []
        self.food_count = 0
        self.lands = []


