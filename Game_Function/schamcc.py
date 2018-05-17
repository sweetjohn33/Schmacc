# A module to hold the processes and phases of the game

from Objects.Deck import Deck
from Objects.Card_classes import NormalCreature
from Objects.Card_classes import EliteCreature
from Objects.Card_classes import BasicCreature
from Objects.Card_classes import Building
from Objects.Card_classes import Spell
from Objects.Land import Land
from random import sample


class Schmacc:

    # This class holds the entire game process. It deals with the decks of cards, the players of the game,
    # and the phases of the turns that players take. All it needs as an input is a number of players
    # (in the form of a string). In the init function you will find lists containing the monsters, buildings,
    # and spells for the game.

    def __init__(self, number):
        """

        :param number: The number of players
        """

        self._number_of_Players = int(number)
        self._Elite_creatures = Deck([EliteCreature("Baby Chicken of Death", 6, 9, 9, "Meadow", "Snow"),
                                         EliteCreature("Armadillo Turtle", 11, 11, 2, "Marsh", "Forest"),
                                         EliteCreature("Ding-aDinga-....Saurus", 6, 4, 14, "Mountain", "Snow"),
                                         EliteCreature("Wan Shi Tong", 10, 10, 4, "Desert", "Marsh"),
                                         EliteCreature("Phoenix", 10, 6, 8, "Desert", "Meadow"),
                                         EliteCreature("Le Flop Dog", 6, 8, 10, "Snow", "Desert"),
                                         EliteCreature("Da Pig", 10, 10, 10, "Meadow", "Snow"),
                                         EliteCreature("Wasabi Ice Cream Dragon", 5, 7, 12, "Snow", "Forest"),
                                         EliteCreature("Mongoose Dragon", 8, 6, 10, "Desert", "Meadow")], "creature")

        self._Normal_creatures = Deck([NormalCreature("Tortuga_Luchadora", 5, 6, 5, "Marsh", "Snow"),
                                          NormalCreature("Baby Phoenix", 8, 5, 3, "Desert", "Meadow"),
                                          NormalCreature("Polar Bear Fruit Salesman", 5, 5, 6, "Snow", "Mountain"),
                                          NormalCreature("Headsman", 3, 6, 7, "Meadow", "Desert"),
                                          NormalCreature("Baby Ice Dragon", 3, 5, 6, "Snow", "Desert"),
                                          NormalCreature("Assassin", 4, 4, 8, "Meadow", "Forest"),
                                          NormalCreature("Trojan Donkey", 8, 4, 2, "Meadow", "Marsh"),
                                          NormalCreature("Fox Deer", 6, 2, 6, "Mountain", "Forest"),
                                          NormalCreature("Big Bad Blowing Butcher", 5, 2, 7, "Mountain", "Forest")
                                          ], "creature")
        self._Basic_creatures = Deck([BasicCreature("El_Flamingodingo", 5, 2, 8, "Meadow", "Snow"),
                                         BasicCreature("Vertebro", 5, 2, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 2, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 2, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 2, 2, "Desert", "Snow"),
                                         BasicCreature("Sneaky Soviet Mole", 4, 6, 2, "Meadow", "Snow"),
                                         BasicCreature("Sneaky Soviet Mole", 4, 6, 2, "Meadow", "Snow"),
                                         BasicCreature("Penguin Knight", 2, 5, 5, "Snow", "Desert"),
                                         BasicCreature("Penguin Knight", 2, 5, 5, "Snow", "Desert"),
                                         BasicCreature("DJ Meow Mix", 4, 4, 4, "Forest", "Snow"),
                                         BasicCreature("DJ Meow Mix", 4, 4, 4, "Forest", "Snow"),
                                         BasicCreature("Guard Dawgs", 7, 1, 4, "Desert", "Mountain"),
                                         BasicCreature("Guard Dawgs", 7, 1, 4, "Desert", "Mountain"),
                                         BasicCreature("Scorpius", 3, 3, 6, "Desert", "Forest"),
                                         BasicCreature("Gogoat", 3, 3, 6, "Mountain", "Marsh"),
                                         BasicCreature("Bush Whacking Nun", 4, 2, 6, "Meadow", "Desert"),
                                         BasicCreature("Platypus-Bear", 5, 2, 5, "Marsh", "Meadow"),
                                         BasicCreature("Platypus-Bear", 5, 2, 5, "Marsh", "Meadow")
                                         ], "creature")
        self._Buildings = Deck([Building("Defense Silo", 12, 4),
                                   Building("Defense Silo", 12, 4),
                                   Building("Defense Silo", 12, 4),
                                   Building("Defense Silo", 12, 4),
                                   Building("Hospital", 20, 2),
                                   Building("Hospital", 20, 2),
                                   Building("Hospital", 20, 2),
                                   Building("Hospital", 20, 2),
                                   Building("Trading Port", 14, 4),
                                   Building("Trading Port", 14, 4),
                                   Building("Trading Port", 14, 4),
                                   Building("Trading Port", 14, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Aquaduct", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Adaptation Laboratory", 12, 4),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Neutered Rabbit Mine", 15, 2),
                                   Building("Farm", 18, 2),
                                   Building("Farm", 18, 2),
                                   Building("Farm", 18, 2),
                                   Building("Farm", 18, 2),
                                   Building("The Wall", 6, 7),
                                   Building("The Wall", 6, 7),
                                   Building("The Wall", 6, 7),
                                   Building("The Wall", 6, 7),
                                   ], "building")
        self._Spells = Deck([Spell("Smite"),
                                Spell("Horny Rabbit 1"),
                                Spell("Horny Rabbit 2"),
                                Spell("Holier Than Thou Rabbit"),
                                Spell("Creature Revival"),
                                Spell("Creature Revival"),
                                Spell("Creature Revival"),
                                Spell("Graveyard Swap"),
                                Spell("Graveyard Swap"),
                                Spell("Harsh Winds"),
                                Spell("Harsh Winds"),
                                Spell("Defense Swap"),
                                Spell("Defense Swap"),
                                Spell("Ability Swap"),
                                Spell("Ability Swap"),
                                Spell("Health Swap"),
                                Spell("Health Swap"),
                                Spell("Offense Swap"),
                                Spell("Wasabi Ice Cream"),
                                Spell("Wasabi Ice Cream"),
                                Spell("Terrain Haggel"),
                                Spell("Terrain Haggel"),
                                Spell("The Snuffer"),
                                Spell("The Snuffer"),
                                Spell("Reflector"),
                                Spell("Reflector"),
                                Spell("No Pain No Gain"),
                                Spell("No Pain No Gain"),
                                Spell("Frost Feet"),
                                Spell("Frost Feet"),
                                Spell("Hail Storm"),
                                Spell("Hail Storm"),
                                Spell("Devastating Heat"),
                                Spell("Devastating Heat"),
                                Spell("Sand Storm"),
                                Spell("Sand Storm"),
                                Spell("Celestial Omegahuru"),
                                Spell("Celestial Omegahuru"),
                                Spell("Foggy Woods"),
                                Spell("Foggy Woods"),
                                ], "spell")
        self._Players = Deck([], "player")
        self._Turn_counter = 0

    def return_number_of_players(self):
        return self._number_of_Players

    def return_turn_counter(self):
        return self._Turn_counter

    def advance_turn_counter(self):
        self._Turn_counter += 1

    def return_spells(self):
        return self._Spells

    def return_players(self):
        return self._Players

    def return_buildings(self):
        return self._Buildings

    def return_basic_creatures(self):
        return self._Basic_creatures

    def return_normal_creatures(self):
        return self._Normal_creatures

    def return_elite_creatures(self):
        return self._Elite_creatures

    def shuffle_deck(self):

        # Shuffles the deck of Spell cards

        self._Spells = sample(self._Spells, len(self._Spells))

    def print_game_state(self):

        # Prints the contents of every player's land and graveyard, next to their name.

        for i in self._Players.return_deck():
            print("\n=======\n\n" + i.name() + "'s shit")
            for a in i.lands():
                a.print_contents_neatly()
            gravyyard = []
            for g in i.graveyard():
                gravyyard.append(g.name())
            print("\n" + i.name() + "'s graveyard: " + ', '.join(gravyyard))

    def print_monster_stats(self):
        for i in self._Players.return_deck():
            print("\n=======\n\n" + i.name() + "'s shit")
            for a in i.lands():
                a.print_monsters_in_depth()





    def check_slots(self, player, card):
        """

        :param player: the player checked
        :param card: the type of card checked
        """

        # If a player attempts to buy a monster or building but all of his lands are full, this function will return
        # False so that the player will not be allowed to buy that building (because there will be nowhere to place it.

        if card == "Creature":
            slots_taken = 0
            for land in player.lands():
                if len(land.monster_slot()) == 1:
                    slots_taken += 1
            if len(player.lands()) == slots_taken:
                return False
            else:
                return True
        if card == "Building":
            slots_taken = 0
            for land in player.lands():
                if len(land.building_slots()) == 2:
                    slots_taken += 1
            if len(player.lands()) == slots_taken:
                return False
            else:
                return True


