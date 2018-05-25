# A module to hold the phases of the game

from Objects.Deck import Deck
from Objects.Land import Land
from Objects.player import Player
from random import randint

# def start_game_random(game):
#     
#     for i in range(game.return_number_of_players()):
#         new_player = Player(i)
#         game.return_players().put_card_on_top(new_player)
#     game.return_players().shuffle_deck()
# 
#     unassigned_lands = Deck([Land("Forest"), Land("Forest"), Land("Meadow"), Land("Meadow"), Land("Mountain"),
#                              Land("Mountain"), Land("Snow"), Land("Snow"), Land("Marsh"), Land("Marsh"), Land("Desert"),
#                              Land("Desert")], "land")
# 
#     while unassigned_lands.return_count() != 0:
#         for player in game.return_players().return_deck():
#             rand_index = randint(0, unassigned_lands.return_count() - 1)
#             player.add_land(unassigned_lands.return_card_in_deck(rand_index))
#             unassigned_lands.take_card_out(rand_index)
#     
#     for player in game.return_players().return_deck():
#         for i in range(len(player.lands())):
#             rand_index = randint(0, game.return_basic_creatures().return_count() - 1)
#             player.add_creature(game.return_basic_creatures().return_deck()[rand_index])
# 
#             game.return_basic_creatures().take_card_out(rand_index)
# 
#             rand_index2 = randint(0, game.return_buildings().return_count() - 1)
#             player.add_building(game.return_buildings().return_deck()[rand_index2])
# 
#             game.return_buildings().take_card_out(rand_index2)
# 
#     for a in range(len(player.creatures())):
#         player.put_monster_on_land(player.creatures()[a])

    

def start_game(game):
    # This function starts the game by first shuffling the spell deck, and then initializing the 12 lands
    # we will play with. Then the game creates a number of players by taking their names as inputs. The game
    # distributes the lands randomly and evenly to the players, and then distributes one random building and one
    # random creature to each player for each land they control. The players then place their monsters and buildings
    # on their land one by one. Then the game is setup!

    print("\n=========\nHere is the order the spell cards should be in:\n")
    print(game.return_spells())
    print("\n=========\n")
    unassigned_lands = Deck([Land("Forest"), Land("Forest"), Land("Meadow"), Land("Meadow"), Land("Mountain"),
                             Land("Mountain"), Land("Snow"), Land("Snow"), Land("Marsh"), Land("Marsh"), Land("Desert"),
                             Land("Desert")], "land")

    # The players are prompted for their names and the game creates a player with each name given,
    # adding it to the list of players

    for i in range(game.return_number_of_players()):
        player_name = input("Please enter Player Name: ")
        new_player = Player(player_name)
        game.return_players().put_card_on_top(new_player)
    game.return_players().shuffle_deck()

    # Every land in the list of lands is assigned randomly to a player and added to their list of lands

    while unassigned_lands.return_count() != 0:
        for player in game.return_players().return_deck():
            rand_index = randint(0, unassigned_lands.return_count() - 1)
            player.add_land(unassigned_lands.return_card_in_deck(rand_index))
            player.lands()[-1].set_owner(player)
            unassigned_lands.take_card_out(rand_index)


    # Each player receives one random land and one random building for every land they own. These objects
    # are stored in the players list of buildings and list of monsters

    for player in game.return_players().return_deck():
        for i in range(len(player.lands())):
            rand_index = randint(0, game.return_basic_creatures().return_count() - 1)
            player.add_creature(game.return_basic_creatures().return_deck()[rand_index])

            game.return_basic_creatures().take_card_out(rand_index)

            rand_index2 = randint(0, game.return_buildings().return_count() - 1)
            player.add_building(game.return_buildings().return_deck()[rand_index2])

            game.return_buildings().take_card_out(rand_index2)

    # The player receives a summary of what he or she received randomly to start the game. Then the player begins
    # choosing where to place his creatures one by one, and then his buildings, until he has no more left to place.
    # Then the next player places his shit

    for player in game.return_players().return_deck():

        print("\nPlayer Name:", player.name())
        print("Creatures:", player.creatures())
        print("Buildings:", player.buildings())
        print("Lands:", player.lands())

        print("\nLet's place " + player.name() + "'s creatures!")

        for a in range(len(player.creatures())):
            player.put_monster_on_land(player.creatures()[a])

        print("\nLet's place " + player.name() + "'s buildings!")

        for a in range(len(player.buildings())):
            player.put_building_on_land_to_start(player.buildings()[a])

    # At the end of this process the program ends with a celebratory note to tell you that you are done setting up
    print("\nCongratulations! you have succeeded in setting up the game without crashing it!"
          "\nNow lets see how you play\n")

    turn_player = game.return_players().return_deck()[game.return_turn_counter() % game.return_players().return_count()]
    building_phase(game, turn_player)

def building_phase(game, turn_player):
    """

    :param game: game being played
    :param turn_player: player taking turn
    :param turn_counter: what turn it is
    :return:
    """
    # This function runs the player through their buildings phase. It starts off by giving the player their
    # neutered rabbits, food, and magic card for the turn. Then it presents the player with several options: to buy
    # something, sell something, tribute something, check the game state, or move onto their own turn.
    print("=======\n")
    print("It is " + turn_player.name()
          + "'s Turn, turn " + str(game.return_turn_counter() + 1) + "\n")

    rabbits_gained = randint(1, 6)
    turn_player.add_rabbits(rabbits_gained)

    turn_player.add_spell(game.return_spells().return_deck()[0])
    print(turn_player.name() + " received a spell card this turn")
    print(turn_player.name() + " now has " + str(len(turn_player.spells())) + " spell(s)\n")
    game.return_spells().take_card_off_top()

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
                           "\n4) Check shit out\n5) See my spells\n6) Buy a land\n7) Send me to the " \
                           "main phase bruh"
    print(turn_player.name() + " has entered the building phase.\nWhat would you like to do?\n")
    g = ""
    tried_before = 0
    while not g.isdigit() or int(g) not in range(1, 8):
        if tried_before > 0:
            print("\nInvalid Input. Try Again!\n")
        print(building_phase_quote)
        g = input("Answer me with a number please:")
        tried_before += 1
    g = int(g)
    while g != 7:

        # If the player inputs 1, they will be asked what kind of card they would like to buy.
        # Then the appropriate buying function will be applied. The player always has options to back out of buying.

        if g == 1:
            print("\nWhat would you like to buy?\n1) Magic Card\n2) Building\n3) Basic Creature"
                  "\n4) Normal Creature\n5) Elite Creature\n6) Nothing, I changed my mind")
            h = int(input("Answer me with a number please:"))

            if h == 1:
                turn_player.buy_something_random(2, game.return_spells())
                h = 6

            elif h == 2:
                if game.check_slots(turn_player, "Building"):
                    turn_player.buy_somthing_specific(10, game.return_buildings())
                else:
                    print("\nYou don't have a free building slot!")
                h = 6

            elif h == 3:
                if game.check_slots(turn_player, "Creature"):
                    turn_player.buy_something_random(5, game.return_basic_creatures())
                else:
                    print("\nYou don't have a free monster slot!")
                h = 6

            elif h == 4:
                if game.check_slots(turn_player, "Creature"):
                    turn_player.buy_something_random(8, game.return_normal_creatures())
                else:
                    print("\nYou dont have a free monster slot!")
                h = 6

            if h == 5:
                if game.check_slots(turn_player, "Creature"):
                    turn_player.buy_something_random(14, game.return_elite_creatures())
                else:
                    print("\nYou dont have a free monster slot!")

            else:
                g = ""
                tried_before = 0
                while not g.isdigit() or int(g) not in range(1, 8):
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
            while not answer.isdigit() or int(answer) not in [1,2,3]:
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
                while not land_index.isdigit() or int(land_index) - 1 not in range(len(turn_player.lands()))\
                        and int(land_index) != 1000:
                    if tried_before > 0:
                        print("Invalid input, Try again!\n")
                    for a in range(len(turn_player.lands())):
                        print(str(a + 1) + ") " + turn_player.lands()[a].name(), ":",
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
                            print(turn_player.name() + " has sold " + land.building_slots()[building_sold].name())
                            if land.building_slots()[building_sold].current_health() < \
                                    land.building_slots()[building_sold].original_health():
                                turn_player.add_rabbits(3)
                            else:
                                turn_player.add_rabbits(5)
                            land.building_slots()[building_sold].return_to_original()
                            game.return_buildings().put_card_on_bottom(land.building_slots()[building_sold])
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
                    spells_to_sell = []
                    for j in range(3):
                        item_sold = ""
                        tried_before = 0
                        while not item_sold.isdigit() or int(item_sold) \
                                not in range(len(turn_player.spells()) + 1) or int(item_sold) == 0:
                            if tried_before > 0:
                                print("Invalid input. Try again!\n")
                            for i in turn_player.spells():
                                print(str(turn_player.spells().index(i) + 1) + ")" + i.name())
                            item_sold = input("\nYou will need to pick 3 spells to sell, Pick one")
                            tried_before += 1
                        item_sold = int(item_sold) - 1
                        spells_to_sell.append(turn_player.spells()[item_sold])
                        turn_player.lose_spells(item_sold)

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
                            game.return_spells().put_card_on_bottom(gorf)
                            del gorf
                        turn_player.add_rabbits(1)
                    else:
                        print("\nIm so sorry we couldn't come to an agreement!\n")
                        for gorf in spells_to_sell:
                            turn_player.spells().put_card_on_bottom(gorf)
                            del gorf
                else:
                    print(turn_player.name() + " doesn't have 3 Spells to sell!\n")

            # If the player doesnt want to sell, they will be returned to the original menu of the building phase

            else:
                g = ""
                tried_before = 0
                while not g.isdigit() or int(g) not in range(1, 8):
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
            while not land_index.isdigit() or int(land_index) - 1 not in range(len(turn_player.lands()))\
                    and int(land_index) != 1000:
                if tried_before > 0:
                    print("Invalid input, Try again!\n")
                for a in range(len(turn_player.lands())):
                    print(str(a + 1) + ") " + turn_player.lands()[a].name(), ":",
                          turn_player.lands()[a].contents())
                print("1000) Never Mind")
                land_index = input("\nFrom which land would you like to ruthlessly murder?")
                tried_before += 1
            land_index = int(land_index) - 1

            # Once the player picks an appropriate land, the monster on that land and its current stats will be
            # displayed. The player will be asked to confirm their decision to tribute.

            if land_index != 999:
                land = turn_player.lands()[land_index]
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
                        turn_player.tribute_monster(game, land)
                        g = ""
                        tried_before = 0
                        while not g.isdigit() or int(g) not in range(1, 8):
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
                        while not g.isdigit() or int(g) not in range(1, 8):
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
                    while not g.isdigit() or int(g) not in range(1, 8):
                        if tried_before > 0:
                            print("\nInvalid Input. Try Again!\n")
                        print(building_phase_quote)
                        g = input("Answer me with a number please:")
                        tried_before += 1
                    g = int(g)
            else:
                g = ""
                tried_before = 0
                while not g.isdigit() or int(g) not in range(1, 8):
                    if tried_before > 0:
                        print("\nInvalid Input. Try Again!\n")
                    print(building_phase_quote)
                    g = input("Answer me with a number please:")
                    tried_before += 1
                g = int(g)

        # If the player wants to check shit out they get a print out of the game state including every player's
        # lands, monsters, and graveyard. Then they are returned to the building phase menu.

        if g == 4:
            game.print_game_state()
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 8):
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
            while not g.isdigit() or int(g) not in range(1, 8):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                print(building_phase_quote)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

        if g == 6:
            if game.check_land_avail():
                if turn_player.rabbit_count() > 2:
                    turn_player.buy_land(game)
                else:
                    print("You don't have enough rabbits bro! get wrekt")
            else:
                print("There are no lands available to buy!")
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 8):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                print(building_phase_quote)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

    check_player_status(game)

    print("The building phase is over, now lets move to the main phase\n\n==========\n\n")
    main_phase(game, turn_player, 1)


def main_phase(game, turn_player, phase_number):
    main_phase_quote_1 = "\nWould you like to activate anything?\n1) Activate Spell\n2) " \
                           "Activate Building effect\n3) Activate Monster effect" \
                           "\n4) Check shit out\n5) See my spells\n6) Send me to the " \
                           "battle phase my dude"
    main_phase_quote_2 = "\nWould you like to activate anything?\n1) Activate Spell\n2) " \
                         "Activate Building effect\n3) Activate Monster effect" \
                         "\n4) Check shit out\n5) See my spells\n6) End my turn my dude"
    print("\n\nTurn: " + str(game.return_turn_counter() + 1) + "\n" + turn_player.name() + " has entered the "
          "main phase, what would you like to do?\n\n")
    g = ""
    tried_before = 0
    while not g.isdigit() or int(g) not in range(1, 8):
        if tried_before > 0:
            print("\nInvalid Input. Try Again!\n")
        if phase_number == 1:
            print(main_phase_quote_1)
        if phase_number == 2:
            print(main_phase_quote_2)
        g = input("Answer me with a number please:")
        tried_before += 1
    g = int(g)
    while g != 6:
        if g == 1:
            # Show the player their spells and prompt them to activate one
            pass

        if g == 2:
            # Show the player their buildings and prompt them to activate a building effect
            pass

        if g == 3:
            # Show the player their monsters and prompt to activate a monster effect
            pass

        if g == 4:
            game.print_game_state()
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 8):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                if phase_number == 1:
                    print(main_phase_quote_1)
                if phase_number == 2:
                    print(main_phase_quote_2)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

        # If the player wants to see their spells they get their spells displayed to them. then they are returned to
        # the building phase menu

        if g == 5:
            turn_player.print_spells_neatly()
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 8):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                if phase_number == 1:
                    print(main_phase_quote_1)
                if phase_number == 2:
                    print(main_phase_quote_2)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

    check_player_status(game)

    if phase_number == 1:
        print("The main phase is over, now lets move to the battle phase\n\n==========\n\n")
        battle_phase(game, turn_player)

    if phase_number == 2:
        print("The second main phase is over, and with it ends your turn and your agency over the board situation"
              "I bid thee adieu")
        game.advance_turn_counter()
        turn_player = game.return_players().return_deck()[game.return_turn_counter() %
                                                          game.return_players().return_count()]
        building_phase(game, turn_player)


def battle_phase(game, turn_player):
    battle_phase_quote = "\nWould you like to attack anything? Cause you probably should its a zero drawback play" \
                         " and if you don't you're a goob" \
                         "\n1) Attack Someone\n2) " \
                         "see monster stats\n3) Check shit out\n4) See my spells\n5) Send me to the " \
                         "second main phase my dude"
    print("\n\nTurn: " + str(game.return_turn_counter() + 1) + "\n" + turn_player.name() + \
          " has entered the battle phase, what would you like to do?\n\n")
    g = ""
    tried_before = 0
    while not g.isdigit() or int(g) not in range(1, 6):
        if tried_before > 0:
            print("\nInvalid Input. Try Again!\n")
        print(battle_phase_quote)
        g = input("Answer me with a number please:")
        tried_before += 1
    g = int(g)
    while g != 5:
        if g == 1:
            turn_player.declare_attack(game.return_players())
            print("The battle phase is over, now lets move to the second main phase\n\n==========\n\n")
            main_phase(game, turn_player, 2)

        if g == 2:
            game.print_monster_stats()
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 6):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                print(battle_phase_quote)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

            # Show the player their buildings and prompt them to activate a building effect

        if g == 3:
            game.print_game_state()
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 6):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                print(battle_phase_quote)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

        # If the player wants to see their spells they get their spells displayed to them. then they are returned to
        # the phase menu

        if g == 4:
            turn_player.print_spells_neatly()
            g = ""
            tried_before = 0
            while not g.isdigit() or int(g) not in range(1, 6):
                if tried_before > 0:
                    print("\nInvalid Input. Try Again!\n")
                print(battle_phase_quote)
                g = input("Answer me with a number please:")
                tried_before += 1
            g = int(g)

    check_player_status(game)
    print("The battle phase is over, now lets move to the second main phase\n\n==========\n\n")
    main_phase(game, turn_player, 2)


def check_player_status(game):
    pist = game.return_players().return_deck()

    for player in game.return_players().return_deck():
        empty_lands = 0
        for land in player.lands():
            if land.check_if_empty():
                empty_lands += 1
        if empty_lands == len(player.lands()):
            print(player.name() + " has been eliminated! Join the losers :P ")
            for j in player.lands():
                game.return_unowned_lands().put_card_on_bottom(j)
            for k in player.graveyard():
                if k.card_class() == "Basic Creature":
                    game.return_basic_creatures().put_card_on_bottom(k)

                if k.card_class() == "Normal Creature":
                    game.return_normal_creatures().put_card_on_bottom(k)

                if k.card_class() == "Elite Creature":
                    game.return_elite_creatures().put_card_on_bottom(k)
            game.return_losers().put_card_on_bottom(game.return_players().return_deck().index(player))
            game.return_players().take_card_out(game.return_players().return_deck().index(player))
    if game.return_players().return_count() == 1:
        print(pist[0].name() + " has won the game!! Congratulations!")
        break
    if game.return_players().return_count() == 0:
        print("The game has ended... In a tie??? woah that's weird")
        break


