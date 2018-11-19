# A module to hold the processes and phases of the game
import Objects.Constants as con

class GameLoop:

    def __init__(self, players, game_board):
        self.players = players
        self.player_index = randint(0, len(players))
        self.active_player = players[self.player_index]
        self.game_board = game_board

    def play(self):
        while not game_over(self.game_board.board)[0]:
            # self.game_board.display()
            # print("{}'s move: ".format(self.active_player.shape))
            self.active_player.turn(self.game_board.board)
            if self.player_index > len(self.players):
                self.player_index = 0
            else:
                self.player_index += 1
            self.active_player = self.players[self.player_index]
        self.print_end_game()

class Schmacc:

    # This class holds the entire game process. It deals with the decks of cards, the players of the game,
    # and the phases of the turns that players take. All it needs as an input is a number of players
    # (in the form of a string). In the init function you will find lists containing the monsters, buildings,
    # and spells for the game.

    def __init__(self, num_players):
        """

        :param number: The number of players
        """

        self.number_of_Players = int(num_players)
        self.elite_creatures = con.ELITE
        self.normal_creatures = con.NORMAL
        self.basic_creatures = con.BASIC
        self.buildings = con.BUILDING
        self.spells = con.SPELL
        self.players = []
        self.losers = []
        self.unowned_lands = []
        self.stack = []
        self.event_log = []
        self.pending_log = []

