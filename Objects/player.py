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
        self._name = name
        self._Neutered_rabbits = 0
        self._graveyard = []
        self._spells = []
        self._buildings = []
        self._creatures = []
        self._food_count = 0
        self._lands = []
        self._buysellmultiplier = 1

    def name(self) -> str:
        return self._name

    def set_name(self, name):
        self._name = name

    def rabbit_count(self) -> int:
        return self._Neutered_rabbits

    def return_buysell(self):
        return self._buysellmultiplier

    def calculate_cost(self, cost):
        new_cost = int(cost * self._buysellmultiplier + .5)
        return new_cost

    def calculate_sell_price(self, sell_price):
        new_sell_price = int(cost / self._buysellmultiplier + .5)
        return new_sell_price

    def add_rabbits(self, number):
        self._Neutered_rabbits += number
        print(self._name + " received " + str(number) + " Neutered Rabbits.")
        print(self._name + " now has " + str(self.rabbit_count()) + " Neutered Rabbit(s)\n")

    def subtract_rabbits(self, number):
        self._Neutered_rabbits -= number
        print( "\n" + self._name + " payed " + str(number) + " Neutered Rabbits.")
        print(self._name + " now has " + str(self.rabbit_count()) + " Neutered Rabbit(s)\n")

    def creatures(self) -> list:
        return self._creatures

    def add_creature(self, creature):
        self._creatures.append(creature)

    def spells(self) -> list:
        return self._spells

    def add_spell(self, spell):
        self._spells.append(spell)

    def lose_spells(self, index):
        del self._spells[index]

    def print_spells_neatly(self):
        spell_name = []
        for i in self._spells:
            spell_name.append(i.name())
        print("\n===========\n" + self._name + "'s spells: " + ", ".join(spell_name)
              + "\n\nBe careful not to let anyone see your spells!\n\n===========\n")

    def lands(self) -> list:
        return self._lands

    def add_land(self, land):
        self._lands.append(land)

    def del_land(self, index):
        del self._lands[index]

    def has_no_empty_lands(self):
        empty_count = 0
        for land in self._lands:
            if land.check_if_empty():
                empty_count += 1
        if empty_count == 0:
            return True
        else:
            return False

    def buildings(self) -> list:
        return self._buildings

    def lose_buildings(self, index):
        del self._buildings[index]

    def add_building(self, building):
        self._buildings.append(building)

    def food(self) -> int:
        return self._food_count

    def add_food(self, j):
        self._food_count += j

    def graveyard(self) -> list:
        return self._graveyard

    def send_to_graveyard(self, monster):
        self._graveyard.append(monster)
        monster.land_switch(None)

    # All of these functions are pretty self-explanatory, they do whatever their name says
    
    def tribute_monster(self, game, land):

        # This function takes a player and a land under that player's control. The player picks a monster from that land
        # Or backs out. Once they pick the monster the player chooses what bonuses he hopes to receive from that monster
        # with the bonuses varying based on that monster's health, and that monster's card_class. The tributed monster
        # has its stats restored to original and is sent to the player's graveyard.

        print(self._name + " has tributed " + land.monster_slot().name())
        print("What would you like to harvest form your Mercilessly Mutilated creature?\n1) Food\n2) Magic Cards")
        decision = input("Pick One")
        while decision not in ["1","2"]:
            print("What would you like to harvest form your Mercilessly Mutilated creature?\n1) Food\n2) Magic Cards\n")
            decision = input("Pick One")
        if decision == "1":
            self.add_food(land.monster_slot().current_health())
            print(self._name + " received " + str(land.monster_slot().current_health()) +
                  " food in exchange for his monster's eternal soul")
        if decision == "2":
            pist = game.return_spells().return_deck()
            if land.monster_slot().card_class() == "Basic Creature":
                if land.monster_slot().current_health() < land.monster_slot().original_health():
                    a = 0
                    tried_before = 0
                    while a == 0:
                        if tried_before > 0:
                            print("\nThe card you input did not match any in the list. Try again\n")
                        spell_name = input("Type in the Name of the Card you want")
                        for i in pist:
                            if spell_name.upper() == i.name().upper() and a == 0:
                                self.add_spell(i)
                                print(self._name + " harvested a " + i.name() +
                                      "from the monster's rotting corpse!")
                                game.return_spells().take_card_out(i)
                                a += 1
                    game.return_spells().shuffle_deck()
                    print(self._name + " now has " + str(
                        len(self.spells())) + " spell(s)\n")

                else:
                    self.add_spell(pist[0])
                    print(self._name + " harvested a spell card from the monster's rotting"
                                               " corpse!")
                    print(self._name + " now has " + str(
                        len(self.spells())) + " spell(s)\n")
                    game.return_spells().take_card_off_top()
            if land.monster_slot().card_class() == "Normal Creature":
                if land.monster_slot().current_health() < land.monster_slot().original_health():
                    drawn_cards = []
                    for i in range(3):
                        drawn_cards.append(pist[0])
                        game.return_spells().take_card_off_top()
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
                        game.return_spells().put_card_on_bottom(drawn_cards[card_discarded])
                        del drawn_cards[card_discarded]
                    for card in drawn_cards:
                        print(self._name + " kept the" + card.name())
                        self.spells().append(card)
                        del card

                else:
                    for i in range(3):
                        self.add_spell(pist[0])
                        print(self._name + " received a "
                              + pist[0].name())
                        game.return_spells().take_card_off_top()
                    for h in range(2):
                        for g in range(len(self.spells())):
                            print(str(g + 1) + ") " + self.spells()[g].name())
                        card_discarded = (int(input("You will need to choose 2 of these cards"
                                                    " to discard, which "
                                                    "will they be?")) - 1)
                        while card_discarded not in range(len(self.spells())):
                            print("\ninvalid input\n")
                            for g in range(len(self.spells())):
                                print(str(g + 1) + ") " + self.spells()[g].name())
                            card_discarded = (int(input("You will need to choose 2 of these cards"
                                                        " to discard, which "
                                                        "will they be?")) - 1)
                        print(self._name + " got rid of "
                              + self.spells()[card_discarded].name())
                        game.return_spells().put_card_on_bottom(self.spells()[card_discarded])
                        self.lose_spells([card_discarded])

            if land.monster_slot().card_class() == "Elite Creature":
                if land.monster_slot().current_health() < land.monster_slot().original_health():
                    drawn_cards = []
                    for i in range(7):
                        drawn_cards.append(pist[0])
                        game.return_spells().take_card_off_top()
                    card_kept = ""
                    while card_kept not in ["1","2","3","4","5","6","7"]:
                        for h in range(len(drawn_cards)):
                            print(str(h + 1) + ") " + drawn_cards[h].name())
                        card_kept = input("Which card would you like to keep?")
                    self.add_spell(drawn_cards[int(card_kept) - 1])
                    print(self._name + " has kept " + drawn_cards[int(card_kept) - 1].name() +
                          " and added it to his hand.")
                    del drawn_cards[int(card_kept) - 1]
                    while len(drawn_cards) > 0:
                        card_placed = ""
                        while int(card_placed) - 1 not in range(len(drawn_cards)):
                            for h in range(len(drawn_cards)):
                                print(str(h + 1) + ") " + drawn_cards[h].name())
                            card_placed = input("Which card would you like to place on top of the deck next?")
                            game.return_spells().put_card_on_top(drawn_cards[int(card_placed) - 1])
                            print(self._name + " has placed " + drawn_cards[int(card_placed) - 1].name() +
                                  " on top of the deck")
                            del drawn_cards[int(card_placed) - 1]
                else:
                    drawn_cards = []
                    for i in range(7):
                        drawn_cards.append(pist[0])
                        game.return_spells().take_card_off_top()
                    card_kept = ""
                    while card_kept not in ["1", "2", "3", "4", "5", "6", "7"]:
                        for h in range(len(drawn_cards)):
                            print(str(h + 1) + ") " + drawn_cards[h].name())
                        card_kept = input("Which card would you like to keep?")
                    self.add_spell(drawn_cards[int(card_kept) - 1])
                    print(self._name + " has kept " + drawn_cards[int(card_kept) - 1].name() +
                          " and added it to his hand.")
                    del drawn_cards[int(card_kept) - 1]
                    while len(drawn_cards) > 0:
                        card_placed = ""
                        while int(card_placed) - 1 not in range(len(drawn_cards)):
                            for h in range(len(drawn_cards)):
                                print(str(h + 1) + ") " + drawn_cards[h].name())
                            card_placed = input("Which card would you like to place on the bottom of the deck next?")
                            game.return_spells().put_card_on_bottom(drawn_cards[int(card_placed) - 1])
                            print(self._name + " has placed " + drawn_cards[int(card_placed) - 1].name() +
                                  " on the bottom of the deck")
                            del drawn_cards[int(card_placed) - 1]

        land.monster_slot().return_to_original()
        self.send_to_graveyard(land.monster_slot())
        land.delete_monster()

    def put_monster_on_land(self, creature):
        """

        :param player: The player who is placing the monster
        :param creature: The monster being placed
        :return:
        """

        # If a player receive/buys a monster, he will need to place it. This function displays the player's lands and
        # asks the player to choose where to place his monster. you can only have one monster on each land.

        creature.set_owner(self)
        placement = ""
        tried_before = 0
        while not placement.isdigit() or int(placement) - 1 not in range(len(self._lands)) or\
                self._lands[int(placement) - 1].length_monster_list() > 0:
            if tried_before > 0:
                if not placement.isdigit():
                    print("Invalid input (not an integer). Try again")
                elif int(placement) - 1 not in range(len(self._lands)):
                    print("\nInvalid input (wrong number bitch) Try again\n")
                elif self._lands[int(placement) - 1].length_monster_list() > 0:
                    print("\nThat section of land already has a creature!\n")
            print("Where would you like to place your", creature.name(), "?\n")
            for i in range(len(self._lands)):
                print(str(i + 1) + ")" + str(self._lands[i]))
            placement = input("Type a number")
            tried_before += 1
        placement = int(placement) - 1
        self._lands[placement].add_monster(creature)
        print("\nYou have placed your", creature.name(), "in the", self._lands[placement])

    def put_building_on_land(self, building):
        """

        :param building: the building placed
        """

        # If a player receive/buys a building, he will need to place it. This function displays the player's lands and
        # asks the player to choose where to place his building. You can have 2 buildings on one land.

        building.set_owner(self)
        placement = ""
        tried_before = 0
        while not placement.isdigit() or int(placement) - 1 not in range(len(self._lands)) or\
                len(self._lands[int(placement) - 1].building_slots()) > 1:
            if tried_before > 0:
                if not placement.isdigit():
                    print("Invalid input (not an integer). Try again")
                elif int(placement) - 1 not in range(len(self._lands)):
                    print("\nInvalid input (wrong number bitch) Try again\n")
                elif len(self._lands[int(placement) - 1].building_slots()) > 1:
                    print("\nThat section of land is full of buildings!\n")
            print("Where would you like to place your", building.name(), "?\n")
            for i in range(len(self._lands)):
                print(str(i + 1) + ")" + str(self._lands[i]))
            placement = input("Type a number")
            tried_before += 1
        placement = int(placement) - 1
        self._lands[placement].add_building(building)
        print("You have placed your", building.name(), "in the", self._lands[placement])

    def put_building_on_land_to_start(self, building):
        """

        :param player: The player who is placing the building
        :param building: the building placed
        :return:
        """

        # Same as the function above except during game setup you can only place one building on each of your lands.

        building.set_owner(self)
        placement = ""
        tried_before = 0
        while not placement.isdigit() or int(placement) - 1 not in range(len(self._lands)) or \
                len(self._lands[int(placement) - 1].building_slots()) > 0:
            if tried_before > 0:
                if not placement.isdigit():
                    print("\nInvalid input (not an integer). Try again\n")
                elif int(placement) - 1 not in range(len(self._lands)):
                    print("\nInvalid input (wrong number bitch) Try again\n")
                elif len(self._lands[int(placement) - 1].building_slots()) > 0:
                    print("\nDuring this phase, you can only place one building on each land you own\n")
            print("Where would you like to place your", building.name(), "?\n")
            for i in range(len(self._lands)):
                print(str(i + 1) + ")" + str(self._lands[i]))
            placement = input("Type a number")
            tried_before += 1
        placement = int(placement) - 1
        self._lands[placement].add_building(building)
        print("\nYou have placed your", building.name(), "in the", self._lands[placement], "\n")
        
    def buy_something_random(self, cost, deck):
        """

        :param cost: rabbit cost of card
        :param player: player buying
        :param deck: deck bought from
        """

        # This function takes a card type, a cost, a player, and a list. It uses the card type and list to
        # determine what the player will be receiving (ie elite creature, or building, or spell, etc.). The player
        # receives that monster and gets to place it. They lose a number of neutered rabbits equal to the
        # cost of what they bought.
        cost = self.calculate_cost(cost)
        pist = deck.return_deck()
        if len(pist) > 0:
            if self.rabbit_count() >= cost:
                self.subtract_rabbits(cost)
                if deck.return_object_type() == "spell":
                    self.add_spell(pist[0])
                    print("\nYou have bought a", pist[0].name() + "\n")
                    deck.take_card_off_top()

                elif deck.return_object_type() == "creature":
                    rand_index = randint(0, len(pist) - 1)
                    self.put_monster_on_land(pist[rand_index])
                    print("\nYou have bought a", pist[rand_index].name() + "\n")
                    deck.take_card_out(rand_index)

                elif deck.return_object_type() == "building":
                    rand_index = randint(0, len(pist) - 1)
                    self.put_building_on_land(pist[rand_index])
                    print("\nYou have bought a", pist[rand_index].name() + "\n")
                    deck.take_card_out(rand_index)
            else:
                print("You need" + str(cost) + "rabbits to buy that! You have" + str(self.rabbit_count()) +
                      "rabbits")
        else:
            print("Sorry folks! Were all out of those!")

    def buy_somthing_specific(self, cost, deck):
        """

                :param cost: rabbit cost of card
                :param player: player buying
                :param deck: deck bought from
                """
        cost = self.calculate_cost(cost)
        pist = deck.return_deck()
        if len(pist) > 0:
            if self.rabbit_count() >= cost:
                self.subtract_rabbits(cost)

                if deck.return_object_type() == "spell":
                    a = 0
                    tried_before = 0
                    while a == 0:
                        if tried_before > 0:
                            print("\nThe card you input did not match any in the list. Try again\n")
                        spell_name = input("Type in the Name of the Card you want")
                        for i in pist:
                            if spell_name.upper() == i.name().upper() and a == 0:
                                self.add_spell(i)
                                deck.take_card_out(i)
                                a += 1
                                print("You have bought a", i.name())
                    deck.shuffle_deck()

                if deck.return_object_type() == "creature":
                    choice = ""
                    tried_before = 0
                    while not choice.isdigit() or int(choice) - 1 not in range(len(pist)):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again\n")
                        for i in range(len(pist)):
                            print(str(i + 1) + ")" + pist[i].name())
                        choice = int(input("\nWhich Creature would you like to buy?\n"))
                        tried_before += 1
                    choice = int(choice) - 1
                    self.put_monster_on_land(pist[choice])
                    print("You have bought a", pist[choice].name())
                    deck.take_card_out(choice)
                    deck.shuffle_deck()

                if deck.return_object_type() == "building":
                    choice = ""
                    tried_before = 0
                    while not choice.isdigit() or int(choice) - 1 not in range(len(pist)):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again\n")
                        for i in range(len(pist)):
                            print(str(i + 1) + ")" + pist[i].name())
                        choice = int(input("\nWhich Building would you like to buy?\n"))
                        tried_before += 1
                    choice = int(choice) - 1
                    self.put_building_on_land(pist[choice])
                    print("You have bought a", pist[choice].name())
                    deck.take_card_out(choice)
                    deck.shuffle_deck()


            else:
                print("You need" + str(cost) + "rabbits to buy that! You have" + str(self.rabbit_count()) +
                      "rabbits")
        else:
            print("Sorry folks! Were all out of those!")


        # Does the same thing as the function above except the player gets to choose what card he buys. So this function
        # displays the list of possible cards to choose from and the player picks one to obtain. In the case of the
        # spell card, there are too many cards to list conveniently, so instead the player inputs the name of the card
        # they want and the function searches for a card with a matching name in the spell deck and adds it to the
        # player's hand.

    def declare_attack(self, deck, game):
        monster = ""
        tried_before = 0
        while not monster.isdigit() or self._lands[int(monster) - 1].length_monster_list == 0 or \
                int(monster) - 1 not in range(len(self._lands)):
            if tried_before > 0:
                if self._lands[int(monster) - 1].length_monster_list() == 0:
                    print("\nThat land don't got no monsters to attack with yo, Try again\n")
                else:
                    print("\nInvalid Input. Try Again\n")
            print("My monsters:\n")
            for i in range(len(self._lands)):
                if self._lands[i].length_monster_list() == 0 :
                    print(str(i + 1) + ")" + self._lands[i].name() + ": empty\n")
                else:
                    print(str(i + 1) + ")" + self._lands[i].name() + ": " + self._lands[i].monster_slot().name() +
                          "(Current Attack " + str(self._lands[i].monster_slot().current_attack()) +
                          "/" + str(self._lands[i].monster_slot().original_attack()) + ")\n")
            monster = input("\nWhat monster do you wanna attack with??\n")
            tried_before += 1
        monster = self._lands[int(monster) - 1].monster_slot()

        pist = deck.return_deck()
        choice = ""
        tried_before = 0
        same_player = 0
        while not choice.isdigit() or int(choice) - 1 not in range(deck.return_count()) or same_player == 1:
            if tried_before > 0:
                if same_player > 0:
                    print("\nThat's you silly, you cant attack yourself! Try Again\n")
                else:
                    print("\nInvalid Input. Try Again\n")
            not_attackable = ""
            for i in range(deck.return_count()):
                if pist[i].player_ID() == self._player_ID:
                    print(str(i + 1) + ")" + pist[i].name() + "    That's you silly, you cant attack yourself!")
                    not_attackable = str(i + 1)
                else:
                    print(str(i + 1) + ")" + pist[i].name())
            choice = input("\nWho would you like to attack?\n")
            tried_before += 1
            if choice == not_attackable:
                same_player += 1
        choice = deck.return_card_in_deck(int(choice) - 1)

        monster2 = ""
        tried_before = 0
        while not monster2.isdigit() or choice.lands()[int(monster2) - 1].length_monster_list == 0 and \
                len(choice.lands()[int(monster2) - 1].building_slots()) == 0 or int(monster2) - 1 \
                not in range(len(choice.lands())):
            if tried_before > 0:
                if self._lands[int(monster) - 1].length_monster_list() == 0:
                    print("\nThat land don't got no monsters to attack yo, Try again\n")
                else:
                    print("\nInvalid Input. Try Again\n")
            print(choice.name() + "'s monsters:")
            for i in range(len(choice.lands())):
                if choice.lands()[i].length_monster_list() == 0:
                    if len(choice.lands()[i].building_slots()) == 0:
                        print(str(i + 1) + ")" + choice.lands()[i].name() + ": empty\n")
                    else:
                        for building in choice.lands()[i].building_slots():
                            print(str(choice.lands()[i].building_slots().index(building) + 1) + ")" +
                                  choice.lands()[i].name() + ": " + building.name() +
                                  "(Current health " + str(building.current_health()) +
                                  "/" + str(building.original_health()) + " || Current Defense: " +
                                  str(building.current_defense()) +
                                  "/" + str(building.original_defense()) + ")\n")
                else:
                    print(str(i + 1) + ")" + choice.lands()[i].name() + ": " + choice.lands()[i].monster_slot().name() +
                          "(Current health " + str(choice.lands()[i].monster_slot().current_health()) +
                          "/" + str(choice.lands()[i].monster_slot().original_health()) + " || Current Defense: " +
                          str(choice.lands()[i].monster_slot().current_defense()) +
                          "/" + str(choice.lands()[i].monster_slot().original_defense()) + ")\n")
            monster2 = input("\nWhat monster do you wanna attack??\n")
            tried_before += 1
        monster2 = int(monster2) - 1
        if choice.lands()[monster2].length_monster_list() > 0:
            attack_target = choice.lands()[monster2].monster_slot()
        elif len(choice.lands()[monster2].building_slots()) > 0:
            tried_before = 0
            building = ""
            while not building.isdigit() or int(building) - 1 not in \
                    range(len(choice.lands()[monster2].building_slots())):
                if tried_before > 0:
                    print("Invalid Input. Try Again.\n")
                for build in choice.lands()[int(monster2)].building_slots():
                    print(str(choice.lands()[monster2].building_slots().index(build) + 1)
                          + ") " + choice.lands()[monster2].name() + ": " + build.name() +
                          "(Current health " + str(build.current_health()) +
                          "/" + str(build.original_health()) + " || Current Defense: " +
                          str(build.current_defense()) +
                          "/" + str(build.original_defense()) + ")\n")
                building = input("Which building would you like to attack?")
            attack_target = choice.lands()[monster2].building_slots()[int(building) - 1]
        monster.combat(attack_target, game)

    def buy_land(self, game):
        print("\n\nLands for sale:")
        print("\nUnowned Lands:\n")
        if game.return_unowned_lands().return_count() == 0:
            print("none\n")
        else:
            for land in game.return_unowned_lands().return_deck():
                print(land.contents())
        for player in game.return_players().return_deck():
            print(player.name() + "'s lands up for grabs:")
            for land in player.lands():
                if land.check_if_empty():
                    print(land.name())
            print("\n")
        sector = ""
        tried_before = 0
        while not sector.isdigit() or int(sector) - 1 not in range(0, game.return_players().return_count() + 1) \
                and int(sector) != 1000:
            if tried_before > 0:
                print("Invalid Input. Try Again")
            print ("\n1) the Unowned Lands Pile")
            for i in range(game.return_players().return_count()):
                print(str(i + 2) + ") " + game.return_players().return_deck()[i].name())
            print("1000) Never mind")
            sector = input("\nWhere do you want to buy from?\n")
            tried_before += 1
        sector = int(sector)
        if game.return_players().return_deck()[sector - 2].name() == self._name:
            print("You can't buy land from yourself silly! Try again")
            pass
        elif game.return_players().return_deck()[sector - 2].has_no_empty_lands():
            print("That sector has no no free lands to buy. Try again")
            pass
        elif sector == 1:
            land = ""
            tried_before = 0
            while not land.isdigit() or int(land) - 1 not in range(game.return_unowned_lands().return_count()):
                if tried_before > 0:
                    print("Invalid input. Try Again")
                for i in range(game.return_unowned_lands().return_count()):
                    print(str(i + 1) + ") " + game.return_unowned_lands().return_deck()[i].name())
                land = input("What land would you like to purchase?")
                tried_before += 1
            land = int(land) - 1
            self.add_land(game.return_unowned_lands().return_lands()[land])
            game.return_unowned_lands().take_card_out(land)
            print(self.name() + " has acquired a new land!")

        elif sector != 1000:
            sector = sector - 2
            player = game.return_players().return_deck()[sector]
            land = ""
            tried_before = 0
            while not land.isdigit() or int(land) - 1 not in range(len(player.lands())) or not \
                    player.lands()[int(land) - 1].check_if_empty():
                if tried_before > 0:
                    print("Invalid input. Try Again")
                for i in range(len(player.lands())):
                    if player.lands()[i].check_if_empty():
                        print(str(i + 1) + ") " + player.lands()[i].name() + ": empty")
                    else:
                        print(str(i + 1) + ") " + player.lands()[i].name() + ": This land is not for sale")
                land = input("What land would you like to purchase?")
                tried_before += 1
            land = int(land) - 1
            if player.lands()[land].owner() == self.name():
                print("You own That land already silly! Try again")
            else:
                self.add_land(player.lands()[land])
                player.del_land(land)
                print(self.name() + " has acquired a new land!")
                self.subtract_rabbits(2)
        else:
            pass

    def feed_creature(self):
        tried_before = 0
        creature_fed = ""
        while not creature_fed.isdigit() or int(creature_fed) - 1 not in range(len(self._lands)):
            print("You have " + str(self._food_count) + "food, who would you like to feed?")
            for land in self._lands:
                print(str(self._lands.index(land)) + ") " + land.name())




