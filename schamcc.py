from player import Player
from Card_classes import NormalCreature
from Card_classes import EliteCreature
from Card_classes import BasicCreature
from Card_classes import Building
from Card_classes import Spell
from random import randint
from Land import Land
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

        self._number_of_players = int(number)
        self._List_of_Elite_creatures = [EliteCreature("Baby Chicken of Death", 6, 9, 9, "Meadow", "Snow"),
                                         EliteCreature("Armadillo Turtle", 11, 11, 2, "Marsh", "Forest"),
                                         EliteCreature("Ding-aDinga-....Saurus", 6, 4, 14, "Mountain", "Snow"),
                                         EliteCreature("Wan Shi Tong", 10, 10, 4, "Desert", "Marsh"),
                                         EliteCreature("Phoenix", 10, 6, 8, "Desert", "Meadow"),
                                         EliteCreature("Le Flop Dog", 6, 8, 10, "Snow", "Desert"),
                                         EliteCreature("Da Pig", 10, 10, 10, "Meadow", "Snow"),
                                         EliteCreature("Wasabi Ice Cream Dragon", 5, 7, 12, "Snow", "Forest"),
                                         EliteCreature("Mongoose Dragon", 8, 6, 10, "Desert", "Meadow")]

        self._List_of_Normal_creatures = [NormalCreature("Tortuga_Luchadora", 5, 6, 5, "Marsh", "Snow"),
                                          NormalCreature("Baby Phoenix", 8, 5, 3, "Desert", "Meadow"),
                                          NormalCreature("Polar Bear Fruit Salesman", 5, 5, 6, "Snow", "Mountain"),
                                          NormalCreature("Headsman", 3, 6, 7, "Meadow", "Desert"),
                                          NormalCreature("Baby Ice Dragon", 3, 5, 6, "Snow", "Desert"),
                                          NormalCreature("Assassin", 4, 4, 8, "Meadow", "Forest"),
                                          NormalCreature("Trojan Donkey", 8, 4, 2, "Meadow", "Marsh"),
                                          NormalCreature("Fox Deer", 6, 2, 6, "Mountain", "Forest"),
                                          NormalCreature("Big Bad Blowing Butcher", 5, 2, 7, "Mountain", "Forest")
                                          ]
        self._List_of_Basic_creatures = [BasicCreature("El_Flamingodingo", 5, 2, 8, "Meadow", "Snow"),
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
                                         ]
        self._List_of_Buildings = [Building("Defense Silo", 12, 4),
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
                                   ]
        self._List_of_Spells = [Spell("Smite"),
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
                                ]
        self._List_of_players = []
        self._Spells_to_sell = []

    def start_game(self):

        # This function starts the game by first shuffling the spell deck, and then initializing the 12 lands
        # we will play with. Then the game creates a number of players by taking their names as inputs. The game
        # distributes the lands randomly and evenly to the players, and then distributes one random building and one
        # random creature to each player for each land they control. The players then place their monsters and buildings
        # on their land one by one. Then the game is setup!

        self.shuffle_deck()
        print("\n=========\nHere is the order the spell cards should be in\n")
        print(self._List_of_Spells)
        print("\n=========\n")
        forest1 = Land("Forest")
        forest2 = Land("Forest")
        meadow1 = Land("Meadow")
        meadow2 = Land("Meadow")
        mountain1 = Land("Mountain")
        mountain2 = Land("Mountain")
        snow1 = Land("Snow")
        snow2 = Land("Snow")
        marsh1 = Land("Marsh")
        marsh2 = Land("Marsh")
        desert1 = Land("Desert")
        desert2 = Land("Desert")
        unassigned_lands = [forest1, forest2, meadow1, meadow2, mountain1,
                            mountain2, snow1, snow2, marsh1, marsh2, desert1, desert2]

        # The players are prompted for their names and the game creates a player with each name given,
        # adding it to the list of players

        for i in range(self._number_of_players):
            player_name = input("Please enter Player Name: ")
            new_player = Player(player_name)
            self._List_of_players.append(new_player)
        self._List_of_players = sample(self._List_of_players, len(self._List_of_players))

        # Every land in the list of lands is assigned randomly to a player and added to their list of lands

        while len(unassigned_lands) != 0:
            for player in self._List_of_players:
                rand_index = randint(0, len(unassigned_lands) - 1)
                player.add_land(unassigned_lands[rand_index])
                del unassigned_lands[rand_index]

        # Each player receives one random land and one random building for every land they own. These objects
        # are stored in the players list of buildings and list of monsters

        for player in self._List_of_players:
            for i in range(len(player.lands())):

                rand_index = randint(0, len(self._List_of_Basic_creatures)-1)
                player.add_creature(self._List_of_Basic_creatures[rand_index])

                del self._List_of_Basic_creatures[rand_index]

                rand_index2 = randint(0, len(self._List_of_Buildings) - 1)
                player.add_building(self._List_of_Buildings[rand_index2])

                del self._List_of_Buildings[rand_index2]

        # The player receives a summary of what he or she received randomly to start the game. Then the player begins
        # choosing where to place his creatures one by one, and then his buildings, until he has no more left to place.
        # Then the next player places his shit

        for player in self._List_of_players:

            print("\nPlayer Name:", player.name())
            print("Creatures:", player.creatures())
            print("Buildings:", player.buildings())
            print("Lands:", player.lands())

            print("\nLet's place " + player.name() + "'s creatures!")

            for a in range(len(player.creatures())):
                self.put_monster_on_land(player, player.creatures()[a])

            print("\nLet's place " + player.name() + "'s buildings!")

            for a in range(len(player.buildings())):
                self.put_building_on_land_to_start(player, player.buildings()[a])

        # At the end of this process the program ends with a celebratory note to tell you that you are done setting up
        print("\nCongratulations! you have succeeded in setting up the game without crashing it!"
              "\nNow lets see how you play\n")

    def shuffle_deck(self):

        # Shuffles the deck of Spell cards

        self._List_of_Spells = sample(self._List_of_Spells, len(self._List_of_Spells))

    def print_game_state(self):

        # Prints the contents of every player's land and graveyard, next to their name.

        for i in self._List_of_players:
            print("\n=======\n\n" + i.name() + "'s shit")
            for a in i.lands():
                a.print_contents_neatly()
            gravyyard = []
            for g in i.graveyard():
                gravyyard.append(g.name())
            print("\n" + i.name() + "'s graveyard: " + ', '.join(gravyyard))

    def put_monster_on_land(self, player, creature):
        """

        :param player: The player who is placing the monster
        :param creature: The monster being placed
        :return:
        """

        # If a player receive/buys a monster, he will need to place it. This function displays the player's lands and
        # asks the player to choose where to place his monster. you can only have one monster on each land.

        placement = ""
        tried_before = 0
        while bool(placement.isdigit()) == 0 or int(placement) - 1 not in range(len(player.lands())) or\
                len(player.lands()[int(placement) - 1].monster_slot()) > 0:
            if tried_before > 0:
                if bool(placement.isdigit()) == 0:
                    print("Invalid input (not an integer). Try again")
                elif int(placement) - 1 not in range(len(player.lands())):
                    print("\nInvalid input (wrong number bitch) Try again\n")
                elif len(player.lands()[int(placement) - 1].monster_slots()) > 0:
                    print("\nThat section of land already has a creature!\n")
            print("Where would you like to place your", creature.name(), "?\n")
            for i in range(len(player.lands())):
                print(str(i + 1) + ")" + str(player.lands()[i]))
            placement = input("Type a number")
            tried_before += 1
        placement = int(placement) - 1
        player.lands()[placement].add_monster(creature)
        print("\nYou have placed your", creature.name(), "in the", player.lands()[placement])

    def put_building_on_land(self, player, building):
        """

        :param player: The player who is placing the building
        :param building: the building placed
        """

        # If a player receive/buys a building, he will need to place it. This function displays the player's lands and
        # asks the player to choose where to place his building. You can have 2 buildings on one land.

        placement = ""
        tried_before = 0
        while bool(placement.isdigit()) == 0 or int(placement) - 1 not in range(len(player.lands())) or\
                len(player.lands()[int(placement) - 1].building_slots()) > 1:
            if tried_before > 0:
                if bool(placement.isdigit()) == 0:
                    print("Invalid input (not an integer). Try again")
                elif int(placement) - 1 not in range(len(player.lands())):
                    print("\nInvalid input (wrong number bitch) Try again\n")
                elif len(player.lands()[int(placement) - 1].building_slots()) > 1:
                    print("\nThat section of land is full of buildings!\n")
            print("Where would you like to place your", building.name(), "?\n")
            for i in range(len(player.lands())):
                print(str(i + 1) + ")" + str(player.lands()[i]))
            placement = input("Type a number")
            tried_before += 1
        placement = int(placement) - 1
        player.lands()[placement].add_building(building)
        print("You have placed your", building.name(), "in the", player.lands()[placement])

    def put_building_on_land_to_start(self, player, building):
        """

        :param player: The player who is placing the building
        :param building: the building placed
        :return:
        """

        # Same as the function above except during game setup you can only place one building on each of your lands.

        placement = ""
        tried_before = 0
        while bool(placement.isdigit()) == 0 or int(placement) - 1 not in range(len(player.lands())) or \
                len(player.lands()[int(placement) - 1].building_slots()) > 0:
            if tried_before > 0:
                if bool(placement.isdigit()) == 0:
                    print("\nInvalid input (not an integer). Try again\n")
                elif int(placement) - 1 not in range(len(player.lands())):
                    print("\nInvalid input (wrong number bitch) Try again\n")
                elif len(player.lands()[int(placement) - 1].building_slots()) > 0:
                    print("\nDuring this phase, you can only place one building on each land you own\n")
            print("Where would you like to place your", building.name(), "?\n")
            for i in range(len(player.lands())):
                print(str(i + 1) + ")" + str(player.lands()[i]))
            placement = input("Type a number")
            tried_before += 1
        placement = int(placement) - 1
        player.lands()[placement].add_building(building)
        print("\nYou have placed your", building.name(), "in the", player.lands()[placement], "\n")

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

    def buy_something_random(self, card, cost, player, pist):
        """

        :param card: type of card bought
        :param cost: cost of card
        :param player: player buying
        :param pist: list bought from
        """

        # This function takes a card type, a cost, a player, and a list. It uses the card type and list to
        # determine what the player will be receiving (ie elite creature, or building, or spell, etc.). The player
        # receives that monster and gets to place it. They lose a number of neutered rabbits equal to the
        # cost of what they bought.

        if len(pist) > 0:
            if player.rabbit_count() >= cost:
                player.subtract_rabbits(cost)
                if card == "Spell":
                    player.add_spell(pist[0])
                    print("You have bought a", pist[0].name())
                    del pist[0]

                elif card == "Creature":
                    rand_index = randint(0, len(pist) - 1)
                    player.add_creature(pist[rand_index])
                    self.put_monster_on_land(player, pist[rand_index])
                    del pist[rand_index]

                elif card == "Building":
                    rand_index = randint(0, len(pist) - 1)
                    player.add_building(pist[rand_index])
                    self.put_building_on_land(player, pist[rand_index])
                    del pist[rand_index]
            else:
                print("You need" + str(cost) + "rabbits to buy that! You have" + str(player.rabbit_count()) +
                      "rabbits")
        else:
            print("Sorry folks! Were all out of those!")

    def buy_somthing_specific(self, card, cost, player, pist):
        """

                :param card: type of card bought
                :param cost: cost of card
                :param player: player buying
                :param pist: list bought from
                """

        # Does the same thing as the function above except the player gets to choose what card he buys. So this function
        # displays the list of possible cards to choose from and the player picks one to obtain. In the case of the
        # spell card, there are too many cards to list conveniently, so instead the player inputs the name of the card
        # they want and the function searches for a card with a mathcing name in the spell deck and adds it to the
        # player's hand.

        if len(pist) > 0:
            if player.rabbit_count() >= cost:
                player.subtract_rabbits(cost)

                if card == "Spell":
                    a = 0
                    tried_before = 0
                    while a == 0:
                        if tried_before > 0:
                            print("\nThe card you input did not match any in the list. Try again\n")
                        spell_name = input("Type in the Name of the Card you want")
                        for i in pist:
                            if spell_name.upper() == i.name().upper() and a == 0:
                                player.add_spell(i)
                                del i
                                a += 1
                                print("You have bought a", i.name())
                    self.shuffle_deck()

                if card == "Creature":
                    choice = ""
                    tried_before = 0
                    while bool(choice.isdigit()) == 0 or int(choice) - 1 not in range(len(pist)):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again\n")
                        for i in range(len(pist)):
                            print(str(i + 1) + ")" + pist[i].name())
                        choice = int(input("\nWhich Creature would you like to buy?\n"))
                        tried_before += 1
                    choice = int(choice) - 1
                    self.put_monster_on_land(player, pist[choice])
                    print("You have bought a", pist[choice].name())
                    del pist[choice]

                if card == "Building":
                    choice = ""
                    tried_before = 0
                    while bool(choice.isdigit()) == 0 or int(choice) - 1 not in range(len(List)):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again\n")
                        for i in range(len(pist)):
                            print(str(i + 1) + ")" + pist[i].name())
                        choice = int(input("\nWhich Building would you like to buy?\n"))
                        tried_before += 1
                    choice = int(choice) - 1
                    self.put_building_on_land(player, pist[choice])
                    print("You have bought a", pist[choice].name())
                    del pist[choice - 1]

            else:
                print("You need" + str(cost) + "rabbits to buy that! You have" + str(player.rabbit_count()) +
                      "rabbits")
        else:
            print("Sorry folks! Were all out of those!")

    def tribute_monster(self, turn_player, land):
        """

        :param turn_player: player tributing
        :param land: land tributing from
        """

        # This function takes a player and a land under that player's control. The player picks a monster from that land
        # Or backs out. Once they pick the monster the player chooses what bonuses he hopes to receive from that monster
        # with the bonuses varying based on that monster's health, and that monster's card_class. The tributed monster
        # has its stats restored to original and is sent to the player's graveyard.

        print(turn_player.name() + " has tributed " + land.monster_slot()[0].name())
        print("What would you like to harvest form your Mercilessly Mutilated creature?\n1) Food\n2) Magic Cards")
        decision = input("Pick One")
        while decision not in ["1","2"]:
            print("What would you like to harvest form your Mercilessly Mutilated creature?\n1) Food\n2) Magic Cards\n")
            decision = input("Pick One")
        if decision == "1":
            turn_player.add_food(land.monster_slot()[0].current_health())
            print(turn_player.name() + " received " + str(land.monster_slot()[0].current_health()) +
                  " food in exchange for his monster's eternal soul")
        if decision == "2":
            if land.monster_slot()[0].card_class() == "Basic Creature":
                if land.monster_slot()[0].current_health() < land.monster_slot()[0].original_health():
                    for i in range(len(self._List_of_Spells)):
                        print(str(i + 1) + ") " + self._List_of_Spells[i])
                    spell = int(input("Have the person next "
                                      "to you pick what spell card you get ;)")) - 1
                    turn_player.add_spell(self._List_of_Spells[spell])
                    print(turn_player.name() + " harvested a " + self._List_of_Spells[spell].name() +
                          "from the monster's rotting corpse!")
                    print(turn_player.name() + " now has " + str(
                        len(turn_player.spells())) + " spell(s)\n")
                    del self._List_of_Spells[spell]
                    self.shuffle_deck()

                else:
                    turn_player.add_spell(self._List_of_Spells[0])
                    print(turn_player.name() + " harvested a spell card from the monster's rotting"
                                               " corpse!")
                    print(turn_player.name() + " now has " + str(
                        len(turn_player.spells())) + " spell(s)\n")
                    del self._List_of_Spells[0]

            if land.monster_slot()[0].card_class() == "Normal Creature":
                if land.monster_slot()[0].current_health() < land.monster_slot()[0].original_health():
                    drawn_cards = []
                    for i in range(3):
                        drawn_cards.append(self._List_of_Spells[0])
                        del self._List_of_Spells[0]
                    for h in range(2):
                        for g in range(len(drawn_cards)):
                            print(str(g + 1) + ") " + drawn_cards[g].name())
                        card_discarded = (int(input("You will need to choose 2 cards"
                                                    " to discard of these three, which "
                                                    "will they be?")) - 1)
                        while card_discarded not in range(len(drawn_cards)):
                            print("\ninvalid input\n")
                            for g in range(len(drawn_cards)):
                                print(str(g + 1) + ") " + drawn_cards[g].name())
                            card_discarded = (int(input("You will need to choose 2 cards"
                                                        " to discard of these three, which "
                                                        "will they be?")) - 1)
                        self._List_of_Spells.append(drawn_cards[card_discarded])
                        del drawn_cards[card_discarded]
                    for card in drawn_cards:
                        print(turn_player.name() + " kept the" + card.name())
                        turn_player.spells().append(card)
                        del card

                else:
                    for i in range(3):
                        turn_player.add_spell(self._List_of_Spells[0])
                        print(turn_player.name() + " received a "
                              + self._List_of_Spells[0].name())
                        del self._List_of_Spells[0]
                    for h in range(2):
                        for g in range(len(turn_player.spells())):
                            print(str(g + 1) + ") " + turn_player.spells()[g].name())
                        card_discarded = (int(input("You will need to choose 2 of these cards"
                                                    " to discard, which "
                                                    "will they be?")) - 1)
                        while card_discarded not in range(len(turn_player.spells())):
                            print("\ninvalid input\n")
                            for g in range(len(turn_player.spells())):
                                print(str(g + 1) + ") " + turn_player.spells()[g].name())
                            card_discarded = (int(input("You will need to choose 2 of these cards"
                                                        " to discard, which "
                                                        "will they be?")) - 1)
                        print(turn_player.name() + " got rid of "
                              + turn_player.spells()[card_discarded].name())
                        self._List_of_Spells.append(turn_player.spells()[card_discarded])
                        del turn_player.spells()[card_discarded]

            if land.monster_slot()[0].card_class() == "Elite Creature":
                if land.monster_slot()[0].current_health() < land.monster_slot()[0].original_health():
                    drawn_cards = []
                    for i in range(7):
                        drawn_cards.append(self._List_of_Spells[0])
                        del self._List_of_Spells[0]
                    card_kept = ""
                    while card_kept not in ["1","2","3","4","5","6","7"]:
                        for h in range(len(drawn_cards)):
                            print(str(h + 1) + ") " + drawn_cards[h].name())
                        card_kept = input("Which card would you like to keep?")
                    turn_player.add_spell(drawn_cards[int(card_kept) - 1])
                    print(turn_player.name() + " has kept " + drawn_cards[int(card_kept) - 1].name() +
                          " and added it to his hand.")
                    del drawn_cards[int(card_kept) - 1]
                    while len(drawn_cards) > 0:
                        card_placed = ""
                        while int(card_placed) - 1 not in range(len(drawn_cards)):
                            for h in range(len(drawn_cards)):
                                print(str(h + 1) + ") " + drawn_cards[h].name())
                            card_placed = input("Which card would you like to place on top of the deck next?")
                            self._List_of_Spells.insert(0,drawn_cards[int(card_placed) - 1])
                            print(turn_player.name() + " has placed " + drawn_cards[int(card_placed) - 1].name() +
                                  " on top of the deck")
                            del drawn_cards[int(card_placed) - 1]
                else:
                    drawn_cards = []
                    for i in range(7):
                        drawn_cards.append(self._List_of_Spells[0])
                        del self._List_of_Spells[0]
                    card_kept = ""
                    while card_kept not in ["1", "2", "3", "4", "5", "6", "7"]:
                        for h in range(len(drawn_cards)):
                            print(str(h + 1) + ") " + drawn_cards[h].name())
                        card_kept = input("Which card would you like to keep?")
                    turn_player.add_spell(drawn_cards[int(card_kept) - 1])
                    print(turn_player.name() + " has kept " + drawn_cards[int(card_kept) - 1].name() +
                          " and added it to his hand.")
                    del drawn_cards[int(card_kept) - 1]
                    while len(drawn_cards) > 0:
                        card_placed = ""
                        while int(card_placed) - 1 not in range(len(drawn_cards)):
                            for h in range(len(drawn_cards)):
                                print(str(h + 1) + ") " + drawn_cards[h].name())
                            card_placed = input("Which card would you like to place on the bottom of the deck next?")
                            self._List_of_Spells.append(drawn_cards[int(card_placed) - 1])
                            print(turn_player.name() + " has placed " + drawn_cards[int(card_placed) - 1].name() +
                                  " on the bottom of the deck")
                            del drawn_cards[int(card_placed) - 1]

        land.monster_slot()[0].return_to_original()
        turn_player.send_to_graveyard(land.monster_slot()[0])
        del land.monster_slot()[0]

    def building_phase(self, turn_player, turn_counter):
        """

        :param turn_player: player taking turn
        :return:
        """

        # This function runs the player through their buildings phase. It starts off by giving the player their
        # neutered rabbits, food, and magic card for the turn. Then it presents the player with several options: to buy
        # something, sell something, tribute something, check the game state, or move onto their own turn.
        print("=======\n")
        print("It is " + turn_player.name()
              + "'s Turn, turn " + str(turn_counter + 1) + "\n")

        rabbits_gained = randint(1, 6)
        turn_player.add_rabbits(rabbits_gained)

        turn_player.add_spell(self._List_of_Spells[0])
        print(turn_player.name() + " received a spell card this turn")
        print(turn_player.name() + " now has " + str(len(turn_player.spells())) + " spell(s)\n")
        del self._List_of_Spells[0]

        food_bonus = 0
        for land in turn_player.lands():
            for building in land.building_slots():
                if building.name() == "Farm":
                    food_bonus += 1
        if food_bonus > 0:
            turn_player.add_food(food_bonus)
            print(turn_player.name() + " received " + str(food_bonus) + " food this turn")
            print(turn_player.name() + " now has " + str(turn_player.food()) + " food\n")

        # Now that the player has received their goodies for the turn, they can decide if they want to buy,
        # sell, or tribute anything

        building_phase_quote = "\nWould you like to buy or sell anything?\n1) Buy something\n2) " \
                               "Sell Something\n3) Brutally Sacrifice a creature to the RNG gods" \
                               "\n4) Check shit out\n5) See my spells\n6) Send me to the " \
                               "main phase bruh"
        print(turn_player.name() + " has entered the building phase.\nWhat would you like to do?\n")
        g = ""
        tried_before = 0
        while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
            if tried_before > 0:
                print("\nInvalid Input. Try Again!\n")
            print(building_phase_quote)
            g = input("Answer me with a number please:")
            tried_before += 1
        g = int(g)
        while g != 6:

            # If the player inputs 1, they will be asked what kind of card they would like to buy.
            # Then the appropriate buying function will be applied. The player always has options to back out of buying.

            if g == 1:
                print("\nWhat would you like to buy?\n1) Magic Card\n2) Building\n3) Basic Creature"
                      "\n4) Normal Creature\n5) Elite Creature\n6) Nothing, I changed my mind")
                h = int(input("Answer me with a number please:"))

                if h == 1:
                    self.buy_something_random("Spell", 2, turn_player, self._List_of_Spells)
                    h = 6

                elif h == 2:
                    if self.check_slots(turn_player, "Building"):
                        self.buy_somthing_specific("Building", 10, turn_player, self._List_of_Buildings)
                    else:
                        print("\nYou don't have a free building slot!")
                    h = 6

                elif h == 3:
                    if self.check_slots(turn_player, "Creature"):
                        self.buy_something_random("Creature", 5, turn_player, self._List_of_Basic_creatures)
                    else:
                        print("\nYou don't have a free monster slot!")
                    h = 6

                elif h == 4:
                    if self.check_slots(turn_player, "Creature"):
                        self.buy_something_random("Creature", 8, turn_player, self._List_of_Normal_creatures)
                    else:
                        print("\nYou dont have a free monster slot!")
                    h = 6

                if h == 5:
                    if self.check_slots(turn_player, "Creature"):
                        self.buy_something_random("Creature", 14, turn_player, self._List_of_Elite_creatures)
                    else:
                        print("\nYou dont have a free monster slot!")

                else:
                    g = ""
                    tried_before = 0
                    while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again!\n")
                        print(building_phase_quote)
                        g = input("Answer me with a number please:")
                        tried_before += 1
                    g = int(g)

            # If the player inputs 2, the game will ask them what type of card they would like to sell.

            if g == 2:
                answer = ""
                tried_before = 0
                while bool(answer.isdigit()) == 0 or int(answer) not in [1,2,3]:
                    if tried_before > 0:
                        print("\nInvalid input. Try again!\n")
                    print("\n1) Building\n2) Magic Card\n3) Never mind\n")
                    answer = input("Which type of card would you like to sell? ")
                    tried_before += 1
                answer = int(answer)

                # If the player wants to sell a building, the game will display their lands and ask from which land they
                # would like to sell. This is too avoid selling wrong copy of a building if a player possesses two
                # of the same building.

                if answer == 1:
                    print("=======\n" + turn_player.name() + "'s shit")
                    land_index = ""
                    tried_before = 0
                    while bool(land_index.isdigit()) == 0 or int(land_index) - 1 not in range(len(turn_player.lands()))\
                            and int(land_index) != 1000:
                        if tried_before > 0:
                            print("Invalid input, Try again!\n")
                        for a in range(len(turn_player.lands())):
                            print(str(a + 1) + ") " + turn_player.lands()[a].return_name(), ":",
                                  turn_player.lands()[a].contents())
                        print("1000) Never Mind")
                        land_index = input("\nFrom which land would you like to sell?")
                        tried_before += 1
                    land_index = int(land_index) - 1

                    # If the player selects a land to sell from, the buildings present on that land will be displayed
                    # with their current health and defense. The player must then decide which of the (max 2) buildings
                    # on that land to sell

                    if land_index != 999:
                        land = turn_player.lands()[land_index]
                        if len(land.building_slots()) != 0:
                            building_sold = ""
                            tried_before = 0
                            while bool(building_sold.isdigit()) == 0 or \
                                    building_sold not in range(len(land.building_slots())) and building_sold != 999:
                                if tried_before > 0:
                                    print("\nInvalid Input. Try Again.\n")
                                for a in range(len(land.building_slots())):
                                    print(str(a + 1) + ") " + land.building_slots()[a].name() + ": Current Health: "
                                          + str(land.building_slots()[a].current_health()) + " Current Defense: " +
                                          str(land.building_slots()[a].current_defense()))
                                print("1000) Never Mind")
                                building_sold = input("Which building would you like to sell?")
                                tried_before += 1
                            building_sold = int(building_sold)

                            # If the player chooses a building to sell, that building will be removed from the land and
                            # returned to the list of buildings with its stats restored to their original values.
                            # If the building was below its full health when it was sold, the player will
                            # receive 3 rabbits. If the health is full, the player receives 5 rabbits.

                            if building_sold != 1000:
                                print(turn_player.name() + " has sold " + land.building_slots()[building_sold].name())
                                if land.building_slots()[building_sold].current_health() < \
                                        land.building_slots()[building_sold].original_health():
                                    turn_player.add_rabbits(3)
                                else:
                                    turn_player.add_rabbits(5)
                                land.building_slots()[building_sold].return_to_original()
                                self._List_of_Buildings.append(land.building_slots()[building_sold])
                                del land.building_slots()[building_sold]
                        else:
                            print("There are no buildings on that land! You should know better!!\n")

                # If the player wants to sell a spell, they will be prompted to pick
                # three spell cards from their hand to sell

                if answer == 2:

                    # If the player has at least three spells, the game will ask the player to inut three spells to sell
                    # Those cards are removed from the player's hand and placed in a list to be held until that list
                    # contains three spell cards.

                    if len(turn_player.spells()) >= 3:
                        for j in range(3):
                            item_sold = ""
                            tried_before = 0
                            while bool(item_sold.isdigit()) == 0 or int(item_sold) \
                                    not in range(len(turn_player.spells()) + 1) or int(item_sold) == 0:
                                if tried_before > 0:
                                    print("Invalid input. Try again!\n")
                                for i in turn_player.spells():
                                    print(str(turn_player.spells().index(i) + 1) + ")" + i.name())
                                item_sold = input("\nYou will need to pick 3 spells to sell, Pick one")
                                tried_before +=1
                            item_sold = int(item_sold) - 1
                            self._Spells_to_sell.append(turn_player.spells()[item_sold])
                            turn_player.lose_spells(item_sold)

                        # When the Spells to sell list reaches length 3, the player will be reminded of which cards
                        # they have chosen and asked to confirm their choice. If they confirm, the spells will be sold
                        # and placed on the bottom of the spell deck, and the player receives 1 neutered rabbit

                        choice = ""
                        tried_before = 0
                        while bool(choice.isdigit()) == 0 or int(choice) not in [1, 2]:
                            if tried_before > 0:
                                print("Invalid input. Try again!\n")
                            print(self._Spells_to_sell + "\n1) Yes\n2) No\n")
                            choice = input("Are you sure you want to sell these cards??")
                            tried_before += 1
                        if int(choice) == 1:
                            for gorf in self._Spells_to_sell:
                                self._List_of_Spells.append(gorf)
                                del gorf
                            turn_player.add_rabbits(1)
                        else:
                            print("\nIm so sorry we couldn't come to an agreement!\n")
                            for gorf in self._Spells_to_sell:
                                turn_player.spells().append(gorf)
                                del gorf
                    else:
                        print(turn_player.name() + " doesn't have 3 Spells to sell!\n")

                # If the player doesnt want to sell, they will be returned to the origiinal menu of the building phase

                if answer == 3:
                    g = ""
                    tried_before = 0
                    while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again!\n")
                        print(building_phase_quote)
                        g = input("Answer me with a number please:")
                        tried_before += 1
                    g = int(g)

                else:
                    g = ""
                    tried_before = 0
                    while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again!\n")
                        print(building_phase_quote)
                        g = input("Answer me with a number please:")
                        tried_before += 1
                    g = int(g)

            # If the player wants to tribute a monster, they will need to pick a land from which to tribute
            # (for reasons specified earlier)

            if g == 3:
                print("=======\n" + turn_player.name() + "'s shit")
                land_index = ""
                tried_before = 0
                while bool(land_index.isdigit()) == 0 or int(land_index) - 1 not in range(len(turn_player.lands()))\
                        and int(land_index) != 1000:
                    if tried_before > 0:
                        print("Invalid input, Try again!\n")
                    for a in range(len(turn_player.lands())):
                        print(str(a + 1) + ") " + turn_player.lands()[a].return_name(), ":",
                              turn_player.lands()[a].contents())
                    print("1000) Never Mind")
                    land_index = input("\nFrom which land would you like to ruthlessly murder?")
                    tried_before += 1
                land_index = int(land_index) - 1

                # Once the player picks an appropriate land, the monster on that land and its current stats will be
                # displayed. The player will be asked to confirm their decision to tribute.

                if land_index != 999:
                    land = turn_player.lands()[land_index]
                    if len(land.monster_slot()) != 0:
                        monster_sold = ""
                        tried_before = 0
                        while bool(monster_sold.isdigit()) == 0 or int(monster_sold) not in [1, 2]:
                            if tried_before > 0:
                                print("Invalid input. Try again!\n")
                            print(land.monster_slot()[0].name() + ": Current Health: "
                                  + str(land.monster_slot()[0].current_health()) + " Current Defense: " +
                                  str(land.monster_slot()[0].current_defense()) + "\n1) Yes\n2) No")
                            monster_sold = input("Are you sure you want to Sack this Mon??")
                            tried_before += 1

                        # If the player confirms their choice. The monster is tributed and the player is returned to
                        # the building phase menu. If they don't confirm they are just sent back to the menu.

                        if int(monster_sold) == 1:
                            self.tribute_monster(turn_player, land)
                            g = ""
                            tried_before = 0
                            while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                                if tried_before > 0:
                                    print("\nInvalid Input. Try Again!\n")
                                print(building_phase_quote)
                                g = input("Answer me with a number please:")
                                tried_before += 1
                            g = int(g)

                        else:
                            print("\nFine, suit yourself\n")
                            g = ""
                            tried_before = 0
                            while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                                if tried_before > 0:
                                    print("\nInvalid Input. Try Again!\n")
                                print(building_phase_quote)
                                g = input("Answer me with a number please:")
                                tried_before += 1
                            g = int(g)

                    else:
                        print("There are no Monsters on that land! You should know better!!\n")
                        g = ""
                        tried_before = 0
                        while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                            if tried_before > 0:
                                print("\nInvalid Input. Try Again!\n")
                            print(building_phase_quote)
                            g = input("Answer me with a number please:")
                            tried_before += 1
                        g = int(g)
                else:
                    g = ""
                    tried_before = 0
                    while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again!\n")
                        print(building_phase_quote)
                        g = input("Answer me with a number please:")
                        tried_before += 1
                    g = int(g)

            # If the player wants to check shit out they get a print out of the game state including every player's
            # lands, monsters, and graveyard. Then they are returned to the building phase menu.

            if g == 4:
                self.print_game_state()
                g = ""
                tried_before = 0
                while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                    if tried_before > 0:
                        print("\nInvalid Input. Try Again!\n")
                    print(building_phase_quote)
                    g = input("Answer me with a number please:")
                    tried_before += 1
                g = int(g)

            # If the player wants to see their spells they get their spells displayed to them. then they are returned to
            # the building phase menu

            if g == 5:
                turn_player.print_spells_neatly()
                g = ""
                tried_before = 0
                while bool(g.isdigit()) == 0 or int(g) not in range(1, 7):
                    if tried_before > 0:
                        print("\nInvalid Input. Try Again!\n")
                    print(building_phase_quote)
                    g = input("Answer me with a number please:")
                    tried_before += 1
                g = int(g)

        print("The building phase is over, now lets move to the main phase")

    def game_sequence(self):

        # This will run the turns of the game in the correct order until a winner is declared. After one player's turn
        # is over the next player in the list will take their turn

        turn_counter = 0
        turn_player = self._List_of_players[turn_counter % len(self._List_of_players)]
        self.building_phase(turn_player, turn_counter)

