from Game_Function.schamcc import Schmacc
from Game_Function.Phases import start_game


# welcome



if __name__ == "__main__":

    print("Welcome to Schmacc! Let's get this shit set up!")
    number_of_players = ""
    tried = 0
    while not number_of_players.isdigit() or int(number_of_players) not in [2, 3, 4, 6]:
        if tried > 0:
            print("\nYou done messed up.  Let's try again:\n")
        number_of_players = input("How many players are playing? (Pick 2, 3, 4, or 6) ")
        tried += 1

    game1 = Schmacc(number_of_players)
    start_game(game1)

