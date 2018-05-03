# A module to hold the player class


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

    def name(self) -> str:
        return self._name

    def set_name(self, name):
        self._name = name

    def rabbit_count(self) -> int:
        return self._Neutered_rabbits

    def add_rabbits(self, number):
        self._Neutered_rabbits += number
        print(self.name() + " received " + str(number) + " Neutered Rabbits.")
        print(self.name() + " now has " + str(self.rabbit_count()) + " Neutered Rabbit(s)\n")

    def subtract_rabbits(self, number):
        self._Neutered_rabbits -= number
        print(self.name() + " payed " + str(number) + " Neutered Rabbits.")
        print(self.name() + " now has " + str(self.rabbit_count()) + " Neutered Rabbit(s)\n")

    def creatures(self) -> list:
        return self._creatures

    def add_creature(self, creature):
        self._creatures.append(creature)

    def spells(self) -> list:
        return self._spells

    def add_spell(self, spell):
        self._spells.append(spell)

    def lose_spells(self, i):
        del self._spells[i]

    def print_spells_neatly(self):
        spell_name = []
        for i in self._spells:
            spell_name.append(i.name())
        print("\n===========\n" + self.name() + "'s spells: " + ", ".join(spell_name)
              + "\n\nBe careful not to let anyone see your spells!\n\n===========\n")

    def lands(self) -> list:
        return self._lands

    def add_land(self, land):
        self._lands.append(land)

    def buildings(self) -> list:
        return self._buildings

    def lose_buildings(self, i):
        del self._buildings[i]

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

    # All of these functions are pretty self-explanatory, they do whatever their name says

