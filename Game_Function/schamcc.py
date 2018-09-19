# A module to hold the processes and phases of the game

from Objects.Deck import Deck
from Objects.Card_classes import NormalCreature
from Objects.Card_classes import EliteCreature
from Objects.Card_classes import BasicCreature
from Objects.Card_classes import Building
from Objects.Card_classes import Spell
from Objects.Land import Land
from random import sample
from Objects.Constants import *


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

        self._Normal_creatures = Deck([NormalCreature("Tortuga_Luchadora", {"add_defense(" : [5, ["self"], 0]}, 5, 6, 5, "Marsh", "Snow"),
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
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
                                         BasicCreature("Vertebro", 5, 5, 2, "Desert", "Snow"),
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
        self._Losers = Deck([], "player")
        self._Unowned_lands = Deck([], "land")
        self._Weather = CLEAR
        self._Previous_weather = CLEAR
        self._Weather_count = 0
        self._Stack = []
        self._Event_log = []
        self._Pending_log = []


    def return_number_of_players(self):
        return self._number_of_Players

    def return_turn_counter(self):
        return self._Turn_counter

    def advance_turn_counter(self):
        self._Turn_counter += 1

    def log_event(self, event):
        self._Event_log.append(event)

    def log_pending_event(self, event):
        self._Pending_log.append(event)

    def merge_pending(self):
        for event in self._Pending_log:
            self._Event_log.append(event)

    def return_spells(self):
        return self._Spells

    def return_players(self):
        return self._Players

    def return_losers(self):
        return self._Losers

    def return_unowned_lands(self):
        return self._Unowned_lands

    def return_buildings(self):
        return self._Buildings

    def return_basic_creatures(self):
        return self._Basic_creatures

    def return_normal_creatures(self):
        return self._Normal_creatures

    def return_elite_creatures(self):
        return self._Elite_creatures

    def print_player_state(self, player):
        
        # Prints the contents of a player's lands and graveyard

        print("\n=======\n\n" + player.name() + "'s shit:\n")
        for a in player.lands():
            a.print_contents_neatly()
        gravyyard = []
        for g in player.graveyard():
            gravyyard.append(g.name())
        print("\n" + player.name() + "'s graveyard: " + ', '.join(gravyyard))

    def print_game_state(self):

        # Prints the contents of every player's land and graveyard, next to their name.

        for i in self._Players.return_deck():
            self.print_player_state(i)

    def print_monster_stats(self):
        for i in self._Players.return_deck():
            print("\n=======\n\n" + i.name() + "'s shit:\n")
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
                if land.length_monster_list() == 1:
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

    def check_land_avail(self):
        player_with_land_for_sale = 0
        for player in self._Players.return_deck():
            available_lands = 0
            for land in player.lands():
                if land.check_if_empty():
                    available_lands += 1
            if available_lands == 0:
                player_with_land_for_sale += 1
        if self._Unowned_lands.return_count() == 0 and player_with_land_for_sale == self._Players.return_count():
            return False
        else:
            return True

    def decrement_weather(self):
        self._Weather_count -= 1
        if self._Weather_count == 0:
            self.change_weather(CLEAR)

    def change_weather(self, weather):
        self._Previous_weather = self._Weather
        self._Weather = weather
        self._Weather_count = 3
        for player in self._Players.return_deck():
            for land in player.lands():
                for monster in land.monster_slot():
                    if self._Previous_weather.other_thing() == monster.good_land() or land.name() == \
                            self._Previous_weather.other_thing():
                        monster.total_boost(-1)
                    if self._Weather.other_thing() == monster.good_land() or land.name() == self._Weather.other_thing():
                        monster.total_boost(1)
                        print(monster.owner().name() + "'s " + monster.name() + " is enjoying the weather!")
                if land.name() == self._Previous_weather.other_thing():
                    for building in land.building_slots():
                        building.total_boost(-1)
                if land.name() == self._Weather.other_thing():
                    for building in land.building_slots():
                        building.total_boost(1)
        print("A MASSIVE " + weather + " has surrounded the battlefield!")

    def trigger_check(self, trigger):
        stack = []
        for player in self._Players.return_deck():
            for land in player.lands():
                for monster in land.monster_slot():
                    for entry in monster.return_effect():
                        if entry[0] == trigger:
                            if entry[5] == "optional":
                                print("1) Yes\n2) No")
                                answer = input("Would" + monster.owner().name() + " like to activate" + monster.name()
                                               + "'s effect?")
                                if answer == 1:
                                    self._Stack.append(monster.pick_target(entry, self))
                            else:
                                self._Stack.append(monster.pick_target(entry, self))
            for spell in player.spells():
                # check spell triggers and prompt spell activations
                for building in land.building_slots():
                    for entry in building.return_effect():
                        if entry[1] == trigger:
                            print("1) Yes\n2) No")
                            answer = input("Would" + building.owner().name() + " like to activate" + building.name()
                                           + "'s effect?")
                            if answer == 1:
                                stack.append(building.pick_target(entry, self))
        for i in range(len(stack)):
            exec(stack.pop())

    def pick_tribute(self, player):
        print("=======\n" + player.name() + "'s shit")
        land_index = ""
        tried_before = 0
        while not land_index.isdigit() or int(land_index) - 1 not in range(len(player.lands())) \
                and int(land_index) != 1000:
            if tried_before > 0:
                print("Invalid input, Try again!\n")
            for a in range(len(player.lands())):
                print(str(a + 1) + ") " + player.lands()[a].name(), ":",
                      player.lands()[a].contents())
            print("1000) Never Mind")
            land_index = input("\nFrom which land would you like to ruthlessly murder?")
            tried_before += 1
        land_index = int(land_index) - 1

        # Once the player picks an appropriate land, the monster on that land and its current stats will be
        # displayed. The player will be asked to confirm their decision to tribute.

        if land_index != 999:
            land = player.lands()[land_index]
            if land.length_monster_list() != 0:
                monster_sold = ""
                tried_before = 0
                while not monster_sold.isdigit() or int(monster_sold) not in [1, 2]:
                    if tried_before > 0:
                        print("Invalid input. Try again!\n")
                    print(land.monster_slot().name() + ": Current Health: "
                          + str(land.monster_slot().current_health()) + " Current Defense: " +
                          str(land.monster_slot().current_defense()) + "\n1) Yes\n2) No")
                    monster_sold = input("Are you sure you want to Sack this Mon??")
                    tried_before += 1

                # If the player confirms their choice. The monster is tributed and the player is returned to
                # the building phase menu. If they don't confirm they are just sent back to the menu.

                if int(monster_sold) == 1:
                    player.tribute_monster(self, land)

                else:
                    print("\nFine, suit yourself\n")


            else:
                print("\nThere are no Monsters on that land! You should know better!!\n")


    # If the player wants to check shit out they get a print out of the game state including every player's
    # lands, monsters, and graveyard. Then they are returned to the building phase menu.
            
    def sell_something(self, card, player):
        if card == "development":
            print("=======\n" + player.name() + "'s shit")
            land_index = ""
            tried_before = 0
            while not land_index.isdigit() or int(land_index) - 1 not in range(len(player.lands())) \
                    and int(land_index) != 1000:
                if tried_before > 0:
                    print("Invalid input, Try again!\n")
                for a in range(len(player.lands())):
                    print(str(a + 1) + ") " + player.lands()[a].name(), ":",
                          player.lands()[a].contents())
                print("1000) Never Mind")
                land_index = input("\nFrom which land would you like to sell?")
                tried_before += 1
            land_index = int(land_index) - 1
    
            # If the player selects a land to sell from, the buildings present on that land will be displayed
            # with their current health and defense. The player must then decide which of the (max 2) buildings
            # on that land to sell
    
            if land_index != 999:
                land = player.lands()[land_index]
                if len(land.building_slots()) != 0:
                    building_sold = ""
                    tried_before = 0
                    while not building_sold.isdigit() or int(building_sold) - 1 not in \
                            range(len(land.building_slots())) and int(building_sold) != 1000:
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again.\n")
                        for a in range(len(land.building_slots())):
                            print(str(a + 1) + ") " + land.building_slots()[a].name() + ": Current Health: "
                                  + str(land.building_slots()[a].current_health()) + " Current Defense: " +
                                  str(land.building_slots()[a].current_defense()))
                        print("1000) Never Mind")
                        building_sold = input("Which building would you like to sell? ")
                        tried_before += 1
                    building_sold = int(building_sold) - 1
    
                    # If the player chooses a building to sell, that building will be removed from the land and
                    # returned to the list of buildings with its stats restored to their original values.
                    # If the building was below its full health when it was sold, the player will
                    # receive 3 rabbits. If the health is full, the player receives 5 rabbits.
    
                    if building_sold != 999:
                        print(player.name() + " has sold " + land.building_slots()[building_sold].name())
                        if land.building_slots()[building_sold].current_health() < \
                                land.building_slots()[building_sold].original_health():
                            sell_price = player.calculate_sell_price(3)
                            player.add_rabbits(sell_price)
                        else:
                            sell_price = player.calculate_sell_price(5)
                            player.add_rabbits(sell_price)
                        land.building_slots()[building_sold].return_to_original()
                        land.building_slots()[building_sold].land_switch(None)
                        self.return_buildings().put_card_on_bottom(land.building_slots()[building_sold])
                        del land.building_slots()[building_sold]
                else:
                    print("There are no buildings on that land! You should know better!!\n")
            # If the player wants to sell a spell, they will be prompted to pick
            # three spell cards from their hand to sell

        if card == "magic":
            # If the player has at least three spells, the game will ask the player to input three spells to sell
            # Those cards are removed from the player's hand and placed in a list to be held until that list
            # contains three spell cards.
            number_to_sell = int(3 * player.return_buysell() + .5)
            if len(player.spells()) >= number_to_sell:
                spells_to_sell = []
                for j in range(number_to_sell):
                    item_sold = ""
                    tried_before = 0
                    while not item_sold.isdigit() or int(item_sold) \
                            not in range(len(player.spells()) + 1) or int(item_sold) == 0:
                        if tried_before > 0:
                            print("Invalid input. Try again!\n")
                        for i in player.spells():
                            print(str(player.spells().index(i) + 1) + ")" + i.name())
                        item_sold = input("\nYou will need to pick 3 spells to sell, Pick one")
                        tried_before += 1
                    item_sold = int(item_sold) - 1
                    spells_to_sell.append(player.spells()[item_sold])
                    player.lose_spells(item_sold)

                # When the Spells to sell list reaches length 3, the player will be reminded of which cards
                # they have chosen and asked to confirm their choice. If they confirm, the spells will be sold
                # and placed on the bottom of the spell deck, and the player receives 1 neutered rabbit

                choice = ""
                tried_before = 0
                while not choice.isdigit() or int(choice) not in [1, 2]:
                    if tried_before > 0:
                        print("Invalid input. Try again!\n")
                    print(spells_to_sell + "\n1) Yes\n2) No\n")
                    choice = input("Are you sure you want to sell these cards??")
                    tried_before += 1
                if int(choice) == 1:
                    for gorf in spells_to_sell:
                        self.return_spells().put_card_on_bottom(gorf)
                        del gorf
                    player.add_rabbits(1)
                else:
                    print("\nIm so sorry we couldn't come to an agreement!\n")
                    for gorf in spells_to_sell:
                        player.spells().put_card_on_bottom(gorf)
                        del gorf
            else:
                print(player.name() + " doesn't have 3 Spells to sell!\n")

            # If the player doesnt want to sell, they will be returned to the original menu of the building phase

        # If the player wants to tribute a monster, they will need to pick a land from which to tribute
        # (for reasons specified earlier)
