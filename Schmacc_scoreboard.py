from random import randint
from Card_classes import PermanentCard
from schamcc import Schmacc

# welcome


if __name__ == "__main__":
    print("Welcome to Schmacc! Let's get this shit set up!")
    number_of_players = ""
    tried = 0
    while bool(number_of_players.isdigit()) == 0 or int(number_of_players) not in [2, 3, 4, 6]:
        if tried > 0:
            print("\nYou done messed up.  Let's try again:\n")
        number_of_players = input("How many players are playing? (Pick 2, 3, 4, or 6) ")
        tried += 1
    game = Schmacc(number_of_players)
    game.start_game()




    game.game_sequence()
